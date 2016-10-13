def checkio(data):
    non_unique = []
    for el in data:
        if data.count(el) > 1:
            non_unique.append(el)
    return non_unique


checkio([1, 2, 3, 1, 3])