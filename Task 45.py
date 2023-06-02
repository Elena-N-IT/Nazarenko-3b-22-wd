name=str(input("Введите имя файла: "))

try:
    file=open(name, 'r')
    text=file.read()
    print(text)

except FileNotFoundError:
    print("Ошибка!")
