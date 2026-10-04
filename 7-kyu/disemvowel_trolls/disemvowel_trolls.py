def disemvowel(string_):
    no_threat = ""
    for letter in string_:
        if letter not in 'aAeEiIoOuU':
            no_threat += letter
    return no_threat