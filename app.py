from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure key



def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password BLOB
        )
    ''')

    conn.commit()
    conn.close()


init_db()  



@app.route('/')
def home():
    return "Go to /login or /register"



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        
        if not username or not password:
            return "Fields cannot be empty!"

       
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed)
            )
            conn.commit()
        except sqlite3.IntegrityError:
            return "User already exists!"

        conn.close()
        return redirect('/login')

    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        conn.close()

        if user:
            stored_password = user[2]

            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                session['user'] = username
                return redirect('/dashboard')

        return "Invalid credentials!"

    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect('/login')



@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)