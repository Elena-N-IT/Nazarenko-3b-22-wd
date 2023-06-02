try:
    number = int(input("Ввод: "))
    print(number*number)

except ValueError:
    print("Ошибка")