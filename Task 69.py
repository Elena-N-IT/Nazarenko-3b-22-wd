# Создайте базу данных для хранения информации о сотрудниках, включающую их имена,
# должности и зарплаты. Затем выведите все имена сотрудников, занимающих должность менеджера.

import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   position TEXT,
                   salary REAL)''')

cursor.execute("INSERT INTO employees (name, position, salary) VALUES ('Петр Иванов', 'Менеджер', 150000)")
cursor.execute("INSERT INTO employees (name, position, salary) VALUES ('Иван Петров', 'Разработчик', 160000)")
cursor.execute("INSERT INTO employees (name, position, salary) VALUES ('Иван Сидоров', 'Менеджер', 155000)")
conn.commit()

cursor.execute("SELECT name FROM employees WHERE position = 'Менеджер'")
rows = cursor.fetchall()

if len(rows) == 0:
    print("Менеджеры отсутствуют.")
else:
    for row in rows:
        print(row[0])

cursor.close()
conn.close()
