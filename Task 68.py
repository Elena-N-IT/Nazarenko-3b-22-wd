# Создайте базу данных для хранения информации о фильмах, включающую их названия,
# жанры и рейтинги. Затем выведите все фильмы выбранного жанра.

import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   genre TEXT,
                   rating REAL)''')

cursor.execute("INSERT INTO movies (title, genre, rating) VALUES ('Гостья из будущего', 'Фантастика', 9.6)")
cursor.execute("INSERT INTO movies (title, genre, rating) VALUES ('С лёгким паром', 'Драма', 9.9)")
cursor.execute("INSERT INTO movies (title, genre, rating) VALUES ('Иван Васильевич меняет профессию', 'Фантастика', 9.9)")
conn.commit()

selected_genre = input("Введите жанр фильмов для вывода: ")
cursor.execute("SELECT * FROM movies WHERE genre = ?", (selected_genre,))
rows = cursor.fetchall()

if len(rows) == 0:
    print("Фильмов данного жанра не найдено.")
else:
    print(f"Фильмы жанра {selected_genre}:")
    for row in rows:
        print("Название:", row[1])
        print("Жанр:", row[2])
        print("Рейтинг:", row[3])
        print()

cursor.close()
conn.close()
