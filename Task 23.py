import random

array=[]

for n in range(10):
    array.append(random.randint(1, 50))

print(array)

x=int(input("Введите число: "))

if x in array:
    print("Число найдено в массиве")
else:
    print("Число не найдено в массиве")