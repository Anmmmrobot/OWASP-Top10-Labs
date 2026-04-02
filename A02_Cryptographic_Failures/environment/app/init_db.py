import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# 明文密码（A02）
users = [
    ("alice", "alice123"),
    ("bob", "bob123"),
    ("admin", "admin123")
]

cur.executemany(
    "INSERT INTO users(username,password) VALUES(?,?)",
    users
)

conn.commit()
conn.close()

print("Database initialized.")
