class Book:

    def __init__(self, title, author, year, genre):
        self.title=title
        self.author=author
        self.year=year
        self.genre=genre

    def info(self):
        print(self.title, self.author, "(", self.year, ")", self.genre)


my_favourite_book=Book("Финансист", "Теодор Драйзер", 2016, "роман")
my_favourite_book.info()