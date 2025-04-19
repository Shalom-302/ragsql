import sqlite3

# Connexion et création de la base
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Création des tables
cursor.execute("DROP TABLE IF EXISTS courses;")
cursor.execute("DROP TABLE IF EXISTS students;")

cursor.execute("""
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
""")

# Données d'exemple
courses = [('Mathematics',), ('Physics',), ('Biology',)]
students = [
    ('Alice', 1), ('Bob', 2), ('Charlie', 1),
    ('Diana', 3), ('Eve', 1), ('Frank', 2)
]

cursor.executemany("INSERT INTO courses (name) VALUES (?)", courses)
cursor.executemany("INSERT INTO students (name, course_id) VALUES (?, ?)", students)

conn.commit()
conn.close()
