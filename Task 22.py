import random

array=[]

for a in range(10):
    array.append(random.randint(1, 10))

print(sum(array))