try:
    with open('test.txt', 'r') as file:
        file.write('Hello, world!')

except FileNotFoundError:
    print("Ошибка!")

except IOError:
    print("Ошибка!")