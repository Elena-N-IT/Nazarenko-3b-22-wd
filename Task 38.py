file=open("text.txt", "r", encoding="utf-8")
text=file.read()
print(text)
file.close()