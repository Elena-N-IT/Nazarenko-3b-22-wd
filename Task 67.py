# Создайте базу данных для хранения информации о книгах, включающую их названия,
# авторов и годы выпуска. Затем выведите все книги, выпущенные после 2000 года.

import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   author TEXT,
                   year INTEGER)''')

cursor.execute("INSERT INTO books (title, author, year) VALUES ('Путешествие Алисы', 'Кир Булычёв', 1974)")
cursor.execute("INSERT INTO books (title, author, year) VALUES ('Хилари Мантел', 'Волчий зал', 2009)")

conn.commit()

cursor.execute("SELECT * FROM books WHERE year > 2000")
rows = cursor.fetchall()

for row in rows:
    print("Название:", row[1])
    print("Автор:", row[2])
    print("Год выпуска:", row[3])
    print()

cursor.close()
conn.close()

