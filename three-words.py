def checkio(words):
    words = words.split(" ")
    i = 0
    for el in words:
        if str.isdigit(el):
            i = 0
        else:
            i += 1
        if i == 3:
            break
    return (i == 3)

print(checkio("Hello World hello"))
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
print(checkio("He is 123 man"))