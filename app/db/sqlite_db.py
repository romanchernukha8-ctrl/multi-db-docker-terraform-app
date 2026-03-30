import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "database.db")


def init_sqlite():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute("INSERT INTO users (name) VALUES (?)", ("SQLite_Bob",))
    conn.commit()

    return conn, cursor


def get_sqlite_data(cursor):
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
