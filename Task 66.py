# Создайте базу данных для хранения информации о студентах, включающую их имена,
# возраст и средний балл. Затем выведите все данные на экран.

import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER,
                   average_score REAL)''')

cursor.execute("INSERT INTO students (name, age, average_score) VALUES ('Иван', 20, 4.5)")
cursor.execute("INSERT INTO students (name, age, average_score) VALUES ('Мария', 19, 4.2)")
cursor.execute("INSERT INTO students (name, age, average_score) VALUES ('Алексей', 21, 3.8)")
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print("Имя:", row[1])
    print("Возраст:", row[2])
    print("Средний балл:", row[3])
    print()

cursor.close()
conn.close()
