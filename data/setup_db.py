import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "database.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount REAL,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
""")

cursor.executemany("INSERT INTO users (name, country) VALUES (?, ?)", [
    ("Alice", "USA"),
    ("Bob", "India"),
    ("Charlie", "USA"),
    ("David", "Canada")
])

cursor.executemany("INSERT INTO orders (user_id, amount, date) VALUES (?, ?, ?)", [
    (1, 100.5, "2024-01-01"),
    (2, 200.0, "2024-02-10"),
    (1, 150.0, "2024-03-15"),
    (3, 300.0, "2024-03-20")
])

cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", [
    ("Laptop", 1000),
    ("Phone", 500),
    ("Tablet", 300)
])

conn.commit()
conn.close()

print("Database setup complete!")