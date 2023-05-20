a=int(input("Введите число: "))
n=0
for b in range(2, a//2+1):
    if a%b==0:
        n=n+1
if n<=0:
    print("Число является простым")
else:
    print("Число не является простым")