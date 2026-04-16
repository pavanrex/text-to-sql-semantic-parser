import sqlite3
import os


def execute_sql(sql: str):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    db_path = os.path.join(BASE_DIR, "data", "database.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    conn.close()

    return rows