import sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_logs (
    question TEXT,
    tool_used TEXT
)
""")

conn.commit()
