import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite")
    cursor = db.cursor()

def create_tables():
    cursor.execute("""
        CREATE TABLE lesson_registrations (
            id INTEGER PRIMARY KEY,
        )
    """)
    db.commit()
