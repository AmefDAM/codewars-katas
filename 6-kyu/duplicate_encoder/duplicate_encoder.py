def duplicate_encode(word):
    coded = ""
    lowered = word.lower()
    for character in lowered:
        quantity = lowered.count(character)
        if quantity == 1:
            coded += "("
        if quantity >1:
            coded += ")"
    return coded