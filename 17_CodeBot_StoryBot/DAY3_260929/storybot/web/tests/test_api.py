"""Core account, ownership, visibility, and token-limit behavior."""

from fastapi.testclient import TestClient

from backend import app as api_module


class FakeEngine:
    def token_count(self, prompt):
        return len(prompt)

    def complete(self, prompt):
        return prompt + " The little fox went home happily."


def test_account_story_and_like_flow(tmp_path, monkeypatch):
    monkeypatch.setenv("STORYBOT_DB_PATH", str(tmp_path / "storybot.sqlite3"))
    monkeypatch.setattr(api_module, "get_engine", lambda: FakeEngine())

    with TestClient(api_module.app) as first, TestClient(api_module.app) as second:
        created = first.post("/api/auth/register", json={
            "email": "alice@example.com", "nickname": "Alice", "password": "secret123"
        })
        assert created.status_code == 201
        assert "Max-Age" not in created.headers["set-cookie"]
        assert first.get("/api/auth/me").json()["nickname"] == "Alice"
        assert second.get("/api/auth/me").status_code == 401

        assert first.post("/api/stories", json={"prompt": "x" * 57, "is_public": True}).status_code == 400
        story = first.post("/api/stories", json={"prompt": "x" * 56, "is_public": False})
        assert story.status_code == 201
        story_id = story.json()["id"]
        assert story.json()["title"] == "x" * 56 + " The little fox went home happily."
        assert len(first.get("/api/stories/mine").json()) == 1
        assert first.get("/api/stories").json() == []
        assert second.get(f"/api/stories/{story_id}").status_code == 404

        assert second.post("/api/auth/register", json={
            "email": "bob@example.com", "nickname": "Bob", "password": "secret456"
        }).status_code == 201
        assert second.patch(f"/api/stories/{story_id}", json={"title": "Stolen"}).status_code == 404
        assert second.delete(f"/api/stories/{story_id}").status_code == 404
        assert second.post(f"/api/stories/{story_id}/like").status_code == 404

        published = first.patch(f"/api/stories/{story_id}", json={
            "title": "Little fox", "body": "Once there was a fox.", "is_public": True
        })
        assert published.status_code == 200
        assert second.get(f"/api/stories/{story_id}").json()["title"] == "Little fox"
        assert second.post(f"/api/stories/{story_id}/like").json()["like_count"] == 1
        assert second.post(f"/api/stories/{story_id}/like").json()["like_count"] == 0
        assert first.post(f"/api/stories/{story_id}/like").json()["like_count"] == 1
        disposable = first.post("/api/stories", json={"prompt": "A story.", "is_public": True}).json()["id"]
        assert first.delete(f"/api/stories/{disposable}").status_code == 200
        assert second.get(f"/api/stories/{disposable}").status_code == 404

        old_cookie = first.cookies.get(api_module.COOKIE_NAME)
        assert first.post("/api/auth/logout").status_code == 200
        assert first.get("/api/auth/me").status_code == 401
        assert first.get("/api/auth/me", headers={"Cookie": f"{api_module.COOKIE_NAME}={old_cookie}"}).status_code == 401
        assert first.post("/api/auth/login", json={"email": "alice@example.com", "password": "secret123"}).status_code == 200
        assert first.patch("/api/auth/me", json={"email": "alice@example.com", "nickname": "Alicia"}).json()["nickname"] == "Alicia"
        assert first.patch("/api/auth/me", json={
            "email": "alice2@example.com", "nickname": "Alicia", "current_password": "secret123"
        }).json()["email"] == "alice2@example.com"
        assert first.patch("/api/auth/password", json={
            "current_password": "secret123", "new_password": "newsecret123"
        }).status_code == 200
        assert first.get("/api/auth/me").status_code == 401
        assert first.post("/api/auth/login", json={"email": "alice2@example.com", "password": "newsecret123"}).status_code == 200
        assert first.request("DELETE", "/api/auth/me", json={"current_password": "newsecret123"}).status_code == 200
        assert first.get("/api/auth/me").status_code == 401
        assert second.get(f"/api/stories/{story_id}").status_code == 404


def test_origin_protection(tmp_path, monkeypatch):
    monkeypatch.setenv("STORYBOT_DB_PATH", str(tmp_path / "storybot.sqlite3"))
    with TestClient(api_module.app) as client:
        response = client.post(
            "/api/auth/login",
            headers={"Origin": "https://untrusted.example"},
            json={"email": "nobody@example.com", "password": "secret123"},
        )
        assert response.status_code == 403
