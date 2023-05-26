string=input("Введите любое слово: ")
vowels_list=["а", "у", "о", "ы",
               "и", "э", "я", "ю", "ё", "е"]
count_vowels=0
consonants_list=["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
count_consonants=0

for i in string:
    if i in vowels_list:
        count_vowels += 1

    if i in consonants_list:
        count_consonants += 1

print("Количество гласных букв:", count_vowels)
print("Количество согласных букв:", count_consonants)