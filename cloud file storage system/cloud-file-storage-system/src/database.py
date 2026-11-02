import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from src.config import DATABASE


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
            """
        )


def create_user(username, password):
    """Returns True if the user was created, False if the username exists."""
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
        return True
    except sqlite3.IntegrityError:
        return False


def verify_user(username, password):
    """Returns the user row if credentials are valid, otherwise None."""
    with get_connection() as conn:
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
    if user and check_password_hash(user["password_hash"], password):
        return user
    return None
