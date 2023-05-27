try:
    file = open("text.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Файл не найден")
else:
    text = file.read()
    print(text)
    file.close()