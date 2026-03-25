import sqlite3
from werkzeug.security import generate_password_hash

# Connect to SQLite database (it will create boda.db if not exists)
conn = sqlite3.connect('boda.db')
c = conn.cursor()

# Create users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert an admin user (hashed password)
hashed_password = generate_password_hash("admin123", method='sha256')
try:
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', hashed_password))
except sqlite3.IntegrityError:
    # Admin already exists
    pass

conn.commit()
conn.close()