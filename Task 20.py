import random

my_list = []

for i in range(10):
    my_list.append(random.randint(1, 100))

print(max(my_list), min(my_list))