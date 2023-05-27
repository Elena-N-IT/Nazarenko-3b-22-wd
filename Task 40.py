try:
    open("test.txt")
except FileNotFoundError:
    print("Файл не найден")
else:
    print("Файл существует")
    file.close ()