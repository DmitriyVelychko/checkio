def checkio(*data):
    if len(data) < 1:
       return 0
    return (max(data) - min(data))

checkio(1, 2, 3)
checkio(5, -5)
checkio(10.2, -2.2, 0, 1.1, 0.5)
checkio()
