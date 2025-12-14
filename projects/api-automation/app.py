import os
import time
import psycopg2
from contextlib import contextmanager

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', '5432'))
DB_NAME = os.getenv('DB_NAME', 'testdb')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'pass')

@contextmanager
def get_conn():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    try:
        yield conn
    finally:
        conn.close()

def init_db() -> None:
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        ''')
        conn.commit()

"""Очистити таблицю перед тестами, щоб уникати конфлікту UNIQUE(email)."""
def clear_users() -> None:
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM users;")
        conn.commit()

def insert_user(name: str, email: str) -> int:
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
            (name, email)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id

def update_user(user_id: int, name: str = None, email: str = None) -> int:
    if name is None and email is None:
        return 0
    fields, params = [], []
    if name is not None:
        fields.append('name=%s')
        params.append(name)
    if email is not None:
        fields.append('email=%s')
        params.append(email)
    params.append(user_id)
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(f"UPDATE users SET {', '.join(fields)} WHERE id=%s;", params)
        affected = cur.rowcount
        conn.commit()
        return affected

def delete_user(user_id: int) -> int:
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(f"DELETE FROM users WHERE id=%s;", (user_id,))
        affected = cur.rowcount
        conn.commit()
        return affected

def select_users() -> list[tuple]:
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name, email FROM users ORDER BY id;")
        return cur.fetchall()

def can_connect(retries: int = 30, delay: float = 1.0) -> bool:
    for _ in range(retries):
        try:
            with get_conn():
                return True
        except Exception:
            time.sleep(delay)
    return False

if __name__ == '__main__':
    if not can_connect():
        raise RuntimeError("Cannot connect to Postgres. Check env vars / network.")
    init_db()

    # Демо-цикл CRUD:
    clear_users()

    uid = insert_user("Alina", "alina@example.com")
    print("Inserted id:", uid)

    print("All users:", select_users())

    update_user(uid, name="Bob")
    print("After update:", select_users())

    delete_user(uid)
    print("After delete:", select_users())

