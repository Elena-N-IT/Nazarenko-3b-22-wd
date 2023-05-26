def symbol_count(string):
    result={}
    for n in string:
        symbol_count=0
        for b in string:
            if n==b:
                symbol_count+=1
            else:
                pass
        result[n]=symbol_count
    return result

print(symbol_count(str(input("Введите текст для подсчета частоты испольования символов: "))))