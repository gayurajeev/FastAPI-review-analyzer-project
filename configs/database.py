import sqlite3

DB_NAME = "sqlite.db"

def get_db_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row 
        print("✅ DB Connected Successfully")
        return conn
    except Exception as e:
        print("❌ DB Connection Failed:", e)
        return None


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    # Insert sample data only if empty
    cursor.execute("SELECT COUNT(*) as count FROM users")
    count = cursor.fetchone()["count"]

    if count == 0:
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Sidharth",))
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Tony Stark",))
        conn.commit()

    conn.close()
