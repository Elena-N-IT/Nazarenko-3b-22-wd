try:
    a=int(input("Введите первое число (делимое): ", ))
    b=int(input("Введите второе число (делитель): ", ))
    c=a/b
    print("Результат деления (частное) равен: ", c)
except Exception:
    print("Ошибка")
finally:
    print("Завершение программы")