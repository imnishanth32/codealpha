from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_db_connection():
    return sqlite3.connect('users.db')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = hash_password(request.form['password'])

    conn = get_db_connection()
    cursor = conn.cursor()

    # ✅ Safe parameterized query
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    return "Login successful" if user else "Invalid credentials"

if __name__ == "__main__":
    app.run()
