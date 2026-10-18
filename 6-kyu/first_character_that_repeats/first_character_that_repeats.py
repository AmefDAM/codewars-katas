def first_dup(s):
    for letter in s:
        quantity = s.count(letter)
        if quantity >1:
            return letter