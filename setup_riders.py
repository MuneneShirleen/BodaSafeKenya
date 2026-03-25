import sqlite3

conn = sqlite3.connect("boda.db")
c = conn.cursor()

# Create riders table
c.execute('''
CREATE TABLE IF NOT EXISTS riders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT,
    motorcycle_type TEXT
)
''')

# Insert some sample riders (optional)
c.execute("INSERT INTO riders (name, location, motorcycle_type) VALUES (?, ?, ?)",
          ("John Doe", "Nairobi", "Bajaj"))
c.execute("INSERT INTO riders (name, location, motorcycle_type) VALUES (?, ?, ?)",
          ("Jane Kamau", "Kikuyu", "TVS"))

conn.commit()
conn.close()

print("Riders table created with sample data!")