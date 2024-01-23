import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(
        Path(__file__).parent.parent / "db.sqlite"
    )
    cursor = db.cursor()

def create_tables():
    cursor.execute("""
        --sql
        DROP TABLE IF EXISTS courses;
    """)
    cursor.execute("""
        --sql
        DROP TABLE IF EXISTS teachers;
    """)
    cursor.execute("""
        --sql
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            duration INTEGER
        );
    """)
    cursor.execute("""
        --sql
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            course_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    """)
    db.commit()

def populate_db():
    cursor.execute("""
        --sql
        INSERT INTO courses (name, description, duration) VALUES
            ("Бекенд", "Описание бекенда", 5),
            ("Фронтенд", "Описание фронтенда", 5),
            ("iOS", "Описание iOS", 6),
            ("Android", "Описание Android", 6),
            ("Тестирование", "Описание тестирования", 4)
        """
    )
    cursor.execute("""
        INSERT INTO teachers (name, course_id) VALUES
        ("Adilet", 1),
        ("Igor", 2),
        ("Alexey", 5)
    """)
    db.commit()


def get_courses():
    cursor.execute("""
        --sql
        SELECT * FROM courses
    """)
    # return cursor.fetchone()
    return cursor.fetchall()


def get_courses_with_teachers():
    cursor.execute("""
        --sql
        SELECT c.name, t.name FROM courses AS c
        JOIN teachers AS t ON c.id = t.course_id
    """)
    return cursor.fetchall()


def get_teachers():
    cursor.execute("""
        --sql
        SELECT c.name, t.name FROM teachers AS t
        JOIN courses AS c ON c.id = t.course_id
    """)
    return cursor.fetchall()


def get_course_data(id: int):
    cursor.execute("""
        --sql
        SELECT name, description, duration FROM courses
        WHERE id = :cid
    """, {"cid": id})
    return cursor.fetchone()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()
    # pprint(get_courses())
    # pprint(get_courses_with_teachers())
    # pprint(get_teachers())
    pprint(get_course_data(1))

# SQL - Structured Query Language Структурированный язык запросов
# СУБД - Система управления базами данных
# Реляцтонные базы данных Ralational databases
# Relation - связь, отношение
# Primary key - первичный ключ
# Foreign key - внешний ключ

# Courses:
# 1, "Бекенд", "Описание бекенда", 5,     1
# 2, "Фронтенд", "Описание фронтенда", 5, 1
# 3, "iOS", "Описание iOS", 6,            2
# 4, "Android", "Описание Android", 6,    4
# 5, "Тестирование", "Описание тестирования", 4, 3

# Teachers:
# 1, "Игорь",
# 2, "Алексей"
# 3, "Нурдин"
# 4, "Бекболот"

