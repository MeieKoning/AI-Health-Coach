import sqlite3

def get_connection(db_name="health_coach.db"):
    return sqlite3.connect(db_name)

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            goal TEXT,
            calories INTEGER,
            form_score INTEGER
        )
    ''')
    conn.commit()
    conn.close()
