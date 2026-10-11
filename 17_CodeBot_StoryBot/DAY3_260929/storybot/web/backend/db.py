"""Small SQLite store for the StoryBot MVP."""

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path


DEFAULT_DB = Path(__file__).resolve().parents[1] / "data" / "storybot.sqlite3"


def database_path() -> Path:
    return Path(os.environ.get("STORYBOT_DB_PATH", DEFAULT_DB)).resolve()


@contextmanager
def connection():
    path = database_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path, timeout=30)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def initialize():
    with connection() as db:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL UNIQUE,
                nickname TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS sessions (
                token_hash TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                expires_at INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS stories (
                id INTEGER PRIMARY KEY,
                author_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                title TEXT NOT NULL,
                body TEXT NOT NULL,
                prompt TEXT NOT NULL,
                is_public INTEGER NOT NULL CHECK(is_public IN (0, 1)),
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS likes (
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                story_id INTEGER NOT NULL REFERENCES stories(id) ON DELETE CASCADE,
                PRIMARY KEY (user_id, story_id)
            );
            CREATE INDEX IF NOT EXISTS stories_public_recent
                ON stories(is_public, created_at DESC, id DESC);
            CREATE INDEX IF NOT EXISTS stories_author_recent
                ON stories(author_id, created_at DESC, id DESC);
            """
        )
