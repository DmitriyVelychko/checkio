def left_join(phrases):
    string = []
    for el in phrases:
        string.append(el.replace("right", "left"))
    return ','.join(string)

left_join(("left", "right", "left", "stop"))