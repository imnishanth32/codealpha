import sqlite3
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password BLOB NOT NULL
)
""")

# Insert sample users
users = [
    ("admin", hash_password("admin123")),
    ("user1", hash_password("password1"))
]

cursor.executemany(
    "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
    users
)

conn.commit()
conn.close()

print("✅ Database initialized.")
