import sqlite3

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # ❌ SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        print("✅ Login successful")
    else:
        print("❌ Invalid credentials")

    conn.close()

login()
