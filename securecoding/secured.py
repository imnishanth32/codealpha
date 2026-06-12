import sqlite3
import bcrypt

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # ✅ Parameterized query
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and check_password(password, result[0]):
        print("✅ Login successful")
    else:
        print("❌ Invalid credentials")

    conn.close()

login()
