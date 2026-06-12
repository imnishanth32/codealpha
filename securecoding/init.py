import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert sample users (securely hashed)
users = [
    ("admin", hash_password("admin123")),
    ("user1", hash_password("password1"))
]

cursor.executemany("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", users)

conn.commit()
conn.close()

print("Database initialized successfully.")
