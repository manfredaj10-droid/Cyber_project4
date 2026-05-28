#  Secure Login System

A secure web-based login and registration system built using Flask, SQLite, and bcrypt. The application allows users to register, log in, access a protected dashboard, and securely log out.

---

##  Features

-  User Registration
-  User Login Authentication
-  Password Hashing using bcrypt
-  SQLite Database Integration
-  Session-Based Authentication
-  SQL Injection Protection
-  Secure Logout Functionality
-  Modern Responsive User Interface

---

##  Technologies Used

- Python
- Flask
- SQLite3
- bcrypt
- HTML5
- CSS3

---

##  Project Structure

```text
Secure-Login-System/
│
├── app.py
├── users.db
├── requirements.txt
│
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
```

---

##  How It Works

### Registration Process

1. User enters username and password.
2. Password is hashed using bcrypt.
3. User information is stored in SQLite database.
4. Duplicate usernames are prevented.

### Login Process

1. User enters credentials.
2. System retrieves user from database.
3. bcrypt verifies the password.
4. Session is created upon successful login.

### Dashboard Access

- Only authenticated users can access the dashboard.
- Unauthorized users are redirected to the login page.

### Logout Process

- Session is destroyed.
- User is redirected back to the login page.

---

##  Security Features

### Password Hashing

Passwords are never stored in plain text.

Example:

```text
Password: Password@123

Stored Value:
$2b$12$T8gS6z3Yh...
```

### SQL Injection Protection

Parameterized queries are used:

```python
cursor.execute(
    "SELECT * FROM users WHERE username=?",
    (username,)
)
```

### Session Management

```python
session['user'] = username
```

Sessions ensure that only authenticated users can access protected pages.

---

##  Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/secure-login-system.git
```

### Step 2: Open Project Folder

```bash
cd secure-login-system
```

### Step 3: Install Dependencies

```bash
pip install flask bcrypt
```

### Step 4: Run Application

```bash
python app.py
```

---

##  Run Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Or directly:

```text
http://127.0.0.1:5000/register
```

```text
http://127.0.0.1:5000/login
```

---

##  Example Workflow

### Register

```text
Username: mja
Password: Password@123
```

↓

Account created successfully

### Login

```text
Username: mja
Password: Password@123
```

↓

Dashboard opens

### Logout

↓

Redirected to Login Page

---

##  Project Objectives

- Understand authentication systems
- Learn password hashing techniques
- Work with databases in Flask
- Implement secure login practices
- Manage user sessions securely

---

