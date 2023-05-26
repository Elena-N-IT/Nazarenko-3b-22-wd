from calculator import addition, subtraction, multiplication, division

n=input("Выберите одну из операций (сложение, вычитание, умножение, деление): ")

if n in ("сложение", "вычитание", "умножение", "деление"):
    a=int(input("Введите значение a: "))
    b=int(input("Введите значение b: "))

    if n=="сложение":
        print(addition(a, b))

    if n=="вычитание":
        print(subtraction(a, b))

    if n=="умножение":
        print(multiplication(a, b))

    if n=="деление":
        print(division(a, b))