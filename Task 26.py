print("Введите первое число:")
a=int(input())
print("Введите второе число:")
b=int(input())
for n in range(2,int(min(a,b))):
    if (int(a)%n==0) and (int(b)%n==0):
        print("Наименьший общий множитель равен:", n)
        exit()