def checkio(data):
    res = 1
    for ch in str(data):
        if ch != '0':
            res *= int(ch)
    return res

checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1