def checkio(numb, radix):
    try:
        result = int(numb, radix)
    except ValueError:
        result = -1
    return result


checkio("AF", 16)
checkio("101", 2)
checkio("101", 5)
checkio("Z", 36)
checkio("AB", 10)
