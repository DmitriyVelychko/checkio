def checkio(number):
    if number % 15 == 0:
        res = "Fizz Buzz"
    elif number % 3 == 0:
        res = "Fizz"
    elif number % 5 == 0:
        res = "Buzz"
    else:
        res = number
    return res

checkio(15)
checkio(6)
checkio(5)
checkio(7)
