"""FastAPI endpoints for the StoryBot web service."""

import hashlib
import os
import re
import secrets
import sqlite3
import time
from contextlib import asynccontextmanager
from pathlib import Path

from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .db import connection, initialize
from .inference import MAX_INPUT_TOKENS, get_engine


COOKIE_NAME = "storybot_session"
SESSION_SERVER_LIFETIME = 30 * 24 * 60 * 60
PASSWORD_HASHER = PasswordHasher()
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

@asynccontextmanager
async def lifespan(_app: FastAPI):
    initialize()
    yield


app = FastAPI(title="StoryBot", lifespan=lifespan)


@app.middleware("http")
async def check_origin(request: Request, call_next):
    if request.method not in {"GET", "HEAD", "OPTIONS"}:
        origin = request.headers.get("origin")
        if origin:
            own_origin = f"{request.url.scheme}://{request.headers.get('host', '')}"
            extras = {
                item.strip().rstrip("/")
                for item in os.environ.get("STORYBOT_ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")
                if item.strip()
            }
            if origin.rstrip("/") not in extras | {own_origin}:
                return JSONResponse(status_code=403, content={"detail": "허용되지 않은 요청 출처입니다."})
    return await call_next(request)


def bad_request(message: str):
    raise HTTPException(status_code=400, detail=message)


def normalized_email(value: str) -> str:
    email = value.strip().lower()
    if len(email) > 254 or not EMAIL_PATTERN.fullmatch(email):
        bad_request("올바른 이메일 주소를 입력해 주세요.")
    return email


def valid_nickname(value: str) -> str:
    nickname = value.strip()
    if not 2 <= len(nickname) <= 30:
        bad_request("닉네임은 2~30자로 입력해 주세요.")
    return nickname


def valid_password(value: str):
    if not 8 <= len(value) <= 128:
        bad_request("비밀번호는 8~128자로 입력해 주세요.")


def verify_password(stored_hash: str, password: str) -> bool:
    try:
        return PASSWORD_HASHER.verify(stored_hash, password)
    except VerificationError:
        return False


def token_hash(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def current_user(request: Request, required: bool = True):
    token = request.cookies.get(COOKIE_NAME)
    user = None
    if token:
        with connection() as db:
            user = db.execute(
                """SELECT u.id, u.email, u.nickname, u.password_hash
                   FROM sessions AS s JOIN users AS u ON u.id = s.user_id
                   WHERE s.token_hash = ? AND s.expires_at > ?""",
                (token_hash(token), int(time.time())),
            ).fetchone()
    if required and user is None:
        raise HTTPException(status_code=401, detail="로그인이 필요합니다.")
    return user


def require_user(request: Request):
    return current_user(request, True)


def user_response(user):
    return {"id": user["id"], "email": user["email"], "nickname": user["nickname"]}


def set_session(response: Response, user_id: int):
    token = secrets.token_urlsafe(32)
    now = int(time.time())
    with connection() as db:
        db.execute("DELETE FROM sessions WHERE expires_at <= ?", (now,))
        db.execute(
            "INSERT INTO sessions (token_hash, user_id, expires_at) VALUES (?, ?, ?)",
            (token_hash(token), user_id, now + SESSION_SERVER_LIFETIME),
        )
    response.set_cookie(
        COOKIE_NAME,
        token,
        path="/api",
        httponly=True,
        secure=os.environ.get("STORYBOT_COOKIE_SECURE") == "1",
        samesite="lax",
    )  # No max_age: browser session cookie.


class RegisterInput(BaseModel):
    email: str
    nickname: str
    password: str


class LoginInput(BaseModel):
    email: str
    password: str


class ProfileInput(BaseModel):
    email: str | None = None
    nickname: str | None = None
    current_password: str | None = None


class PasswordInput(BaseModel):
    current_password: str
    new_password: str


class DeleteAccountInput(BaseModel):
    current_password: str


class GenerateInput(BaseModel):
    prompt: str
    is_public: bool


class StoryUpdateInput(BaseModel):
    title: str | None = None
    body: str | None = None
    is_public: bool | None = None


@app.post("/api/auth/register", status_code=201)
def register(data: RegisterInput, response: Response):
    email = normalized_email(data.email)
    nickname = valid_nickname(data.nickname)
    valid_password(data.password)
    try:
        with connection() as db:
            cursor = db.execute(
                "INSERT INTO users (email, nickname, password_hash) VALUES (?, ?, ?)",
                (email, nickname, PASSWORD_HASHER.hash(data.password)),
            )
            user_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="이미 가입된 이메일입니다.")
    set_session(response, user_id)
    return {"id": user_id, "email": email, "nickname": nickname}


@app.post("/api/auth/login")
def login(data: LoginInput, response: Response):
    email = normalized_email(data.email)
    with connection() as db:
        user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if user is None or not verify_password(user["password_hash"], data.password):
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호를 확인해 주세요.")
    set_session(response, user["id"])
    return user_response(user)


@app.post("/api/auth/logout")
def logout(request: Request, response: Response):
    token = request.cookies.get(COOKIE_NAME)
    if token:
        with connection() as db:
            db.execute("DELETE FROM sessions WHERE token_hash = ?", (token_hash(token),))
    response.delete_cookie(COOKIE_NAME, path="/api")
    return {"ok": True}


@app.get("/api/auth/me")
def me(user=Depends(require_user)):
    return user_response(user)


@app.patch("/api/auth/me")
def update_profile(data: ProfileInput, user=Depends(require_user)):
    if data.email is None and data.nickname is None:
        bad_request("변경할 정보를 입력해 주세요.")
    email = user["email"]
    nickname = user["nickname"]
    if data.email is not None:
        email = normalized_email(data.email)
        if email != user["email"] and (
            not data.current_password or not verify_password(user["password_hash"], data.current_password)
        ):
            bad_request("이메일 변경에는 현재 비밀번호가 필요합니다.")
    if data.nickname is not None:
        nickname = valid_nickname(data.nickname)
    try:
        with connection() as db:
            db.execute("UPDATE users SET email = ?, nickname = ? WHERE id = ?", (email, nickname, user["id"]))
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="이미 사용 중인 이메일입니다.")
    return {"id": user["id"], "email": email, "nickname": nickname}


@app.patch("/api/auth/password")
def change_password(data: PasswordInput, request: Request, response: Response, user=Depends(require_user)):
    if not verify_password(user["password_hash"], data.current_password):
        bad_request("현재 비밀번호가 올바르지 않습니다.")
    valid_password(data.new_password)
    with connection() as db:
        db.execute(
            "UPDATE users SET password_hash = ? WHERE id = ?",
            (PASSWORD_HASHER.hash(data.new_password), user["id"]),
        )
        db.execute("DELETE FROM sessions WHERE user_id = ?", (user["id"],))
    response.delete_cookie(COOKIE_NAME, path="/api")
    return {"ok": True, "message": "비밀번호가 변경되었습니다. 다시 로그인해 주세요."}


@app.delete("/api/auth/me")
def delete_account(data: DeleteAccountInput, response: Response, user=Depends(require_user)):
    if not verify_password(user["password_hash"], data.current_password):
        bad_request("현재 비밀번호가 올바르지 않습니다.")
    with connection() as db:
        db.execute("DELETE FROM users WHERE id = ?", (user["id"],))
    response.delete_cookie(COOKIE_NAME, path="/api")
    return {"ok": True}


def story_response(db, row, viewer_id: int | None):
    liked = False
    if viewer_id is not None:
        liked = db.execute(
            "SELECT 1 FROM likes WHERE user_id = ? AND story_id = ?", (viewer_id, row["id"])
        ).fetchone() is not None
    like_count = db.execute("SELECT COUNT(*) FROM likes WHERE story_id = ?", (row["id"],)).fetchone()[0]
    return {
        "id": row["id"],
        "author_id": row["author_id"],
        "author_nickname": row["nickname"],
        "title": row["title"],
        "body": row["body"],
        "prompt": row["prompt"],
        "is_public": bool(row["is_public"]),
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
        "like_count": like_count,
        "liked_by_me": liked,
    }


def story_row(db, story_id: int):
    return db.execute(
        """SELECT s.*, u.nickname FROM stories AS s
           JOIN users AS u ON u.id = s.author_id WHERE s.id = ?""",
        (story_id,),
    ).fetchone()


def automatic_title(body: str) -> str:
    first = re.split(r"(?<=[.!?])\s+", body.strip(), maxsplit=1)[0].strip()
    first = first or "Untitled story"
    return first if len(first) <= 100 else first[:99].rstrip() + "…"


@app.get("/api/stories")
def public_stories(request: Request):
    viewer = current_user(request, required=False)
    viewer_id = viewer["id"] if viewer else None
    with connection() as db:
        rows = db.execute(
            """SELECT s.*, u.nickname FROM stories AS s JOIN users AS u ON u.id = s.author_id
               WHERE s.is_public = 1 ORDER BY s.created_at DESC, s.id DESC"""
        ).fetchall()
        return [story_response(db, row, viewer_id) for row in rows]


@app.get("/api/stories/mine")
def my_stories(user=Depends(require_user)):
    with connection() as db:
        rows = db.execute(
            """SELECT s.*, u.nickname FROM stories AS s JOIN users AS u ON u.id = s.author_id
               WHERE s.author_id = ? ORDER BY s.created_at DESC, s.id DESC""",
            (user["id"],),
        ).fetchall()
        return [story_response(db, row, user["id"]) for row in rows]


@app.post("/api/stories", status_code=201)
def create_story(data: GenerateInput, user=Depends(require_user)):
    if not data.prompt.strip():
        bad_request("이야기의 첫 문장을 입력해 주세요.")
    if "<|endoftext|>" in data.prompt:
        bad_request("입력에 모델 종료 표식을 사용할 수 없습니다.")
    try:
        engine = get_engine()
        count = engine.token_count(data.prompt)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="스토리봇 모델을 준비하지 못했습니다.") from exc
    if count > MAX_INPUT_TOKENS:
        bad_request(f"첫 문장은 최대 {MAX_INPUT_TOKENS}토큰입니다. 현재 {count}토큰입니다.")
    try:
        body = engine.complete(data.prompt)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="이야기를 생성하지 못했습니다. 다시 시도해 주세요.") from exc
    if not body.strip():
        raise HTTPException(status_code=503, detail="빈 이야기가 생성되었습니다. 다시 시도해 주세요.")
    title = automatic_title(body)
    with connection() as db:
        cursor = db.execute(
            "INSERT INTO stories (author_id, title, body, prompt, is_public) VALUES (?, ?, ?, ?, ?)",
            (user["id"], title, body, data.prompt, int(data.is_public)),
        )
        row = story_row(db, cursor.lastrowid)
        return story_response(db, row, user["id"])


@app.get("/api/stories/{story_id}")
def get_story(story_id: int, request: Request):
    viewer = current_user(request, required=False)
    viewer_id = viewer["id"] if viewer else None
    with connection() as db:
        row = story_row(db, story_id)
        if row is None or (not row["is_public"] and row["author_id"] != viewer_id):
            raise HTTPException(status_code=404, detail="스토리를 찾을 수 없습니다.")
        return story_response(db, row, viewer_id)


@app.patch("/api/stories/{story_id}")
def update_story(story_id: int, data: StoryUpdateInput, user=Depends(require_user)):
    with connection() as db:
        row = story_row(db, story_id)
        if row is None or row["author_id"] != user["id"]:
            raise HTTPException(status_code=404, detail="스토리를 찾을 수 없습니다.")
        title = row["title"] if data.title is None else data.title.strip()
        body = row["body"] if data.body is None else data.body
        visibility = row["is_public"] if data.is_public is None else int(data.is_public)
        if not title or len(title) > 120:
            bad_request("제목은 1~120자로 입력해 주세요.")
        if not body.strip() or len(body) > 20000:
            bad_request("본문은 1~20000자로 입력해 주세요.")
        db.execute(
            """UPDATE stories SET title = ?, body = ?, is_public = ?,
               updated_at = datetime('now') WHERE id = ?""",
            (title, body, visibility, story_id),
        )
        return story_response(db, story_row(db, story_id), user["id"])


@app.delete("/api/stories/{story_id}")
def delete_story(story_id: int, user=Depends(require_user)):
    with connection() as db:
        row = story_row(db, story_id)
        if row is None or row["author_id"] != user["id"]:
            raise HTTPException(status_code=404, detail="스토리를 찾을 수 없습니다.")
        db.execute("DELETE FROM stories WHERE id = ?", (story_id,))
    return {"ok": True}


@app.post("/api/stories/{story_id}/like")
def toggle_like(story_id: int, user=Depends(require_user)):
    with connection() as db:
        row = story_row(db, story_id)
        if row is None or not row["is_public"]:
            raise HTTPException(status_code=404, detail="공개 스토리를 찾을 수 없습니다.")
        existing = db.execute(
            "SELECT 1 FROM likes WHERE user_id = ? AND story_id = ?", (user["id"], story_id)
        ).fetchone()
        if existing:
            db.execute("DELETE FROM likes WHERE user_id = ? AND story_id = ?", (user["id"], story_id))
        else:
            db.execute("INSERT INTO likes (user_id, story_id) VALUES (?, ?)", (user["id"], story_id))
        return story_response(db, row, user["id"])


DIST = Path(__file__).resolve().parents[1] / "frontend" / "dist"
if DIST.exists():
    app.mount("/assets", StaticFiles(directory=DIST / "assets"), name="assets")

    @app.get("/{path:path}", include_in_schema=False)
    def frontend(path: str):
        file = (DIST / path).resolve()
        if file.is_file() and file.is_relative_to(DIST):
            return FileResponse(file)
        return FileResponse(DIST / "index.html")
