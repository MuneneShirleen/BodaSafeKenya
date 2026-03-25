from werkzeug.security import generate_password_hash
import sqlite3

conn = sqlite3.connect('boda.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

hashed_password = generate_password_hash("admin123", method='pbkdf2:sha256')

try:
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', hashed_password))
except sqlite3.IntegrityError:
    pass

conn.commit()
conn.close()

print("Database setup complete! Users table created.")