import sqlite3
import os

# Ensure the 'data' folder exists
os.makedirs("data", exist_ok=True)

# Connect to (or create) the SQLite DB
conn = sqlite3.connect("data/example.db")
cursor = conn.cursor()

# Create a table called 'users'
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Insert sample rows
cursor.execute("INSERT INTO users (name, email) VALUES ('Sharon', 'sharon@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Adi', 'adi@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Dana', 'dana@example.com')")
conn.commit()
conn.close()

print("✅ example.db created with 3 users.")