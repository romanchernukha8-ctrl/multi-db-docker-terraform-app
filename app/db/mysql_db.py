import os
import time
import mysql.connector
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


def connect_mysql():
    while True:
        try:
            conn = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST", "127.0.0.1"),
                port=int(os.getenv("MYSQL_PORT", "3309")),
                user=os.getenv("MYSQL_USER", "root"),
                password=os.getenv("MYSQL_PASSWORD", "rootpass"),
                database=os.getenv("MYSQL_DB", "testdb")
            )

            print("MySQL connected!", flush=True)
            return conn

        except Exception as e:
            print("Waiting for MySQL...", e, flush=True)
            time.sleep(5)


def init_mysql(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
    """)

    cursor.execute("INSERT INTO users (name) VALUES (%s)", ("MySQL_Alice",))
    conn.commit()

    return cursor


def get_mysql_data(cursor):
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
