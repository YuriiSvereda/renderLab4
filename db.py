import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")  # зчитується з Render або .env

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def create_users_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                );
            """)

def insert_user(name, email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))


def get_all_data():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name, email FROM users")
            return cur.fetchall()

def insert_data(name, email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))