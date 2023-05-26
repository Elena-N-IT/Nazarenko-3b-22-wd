def reverse_string(string):
    n=""
    for i in reversed(string):
        n+=i
    return n


reverse_string1=reverse_string("Счастье")

print(reverse_string1)