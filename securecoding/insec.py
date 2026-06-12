import sqlite3
import bcrypt

def check_password(password, hashed):
    # ✅ Fix: ensure hashed password is bytes
    if isinstance(hashed, str):
        hashed = hashed.encode()

    return bcrypt.checkpw(password.encode(), hashed)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # ✅ Secure query (prevents SQL injection)
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    if result and check_password(password, result[0]):
        print("✅ Login successful")
    else:
        print("❌ Invalid credentials")

if __name__ == "__main__":
    login()
