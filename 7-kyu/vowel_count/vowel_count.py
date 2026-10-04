def get_count(sentence):
    vowels = 0
    for letter in sentence:
        if letter in "aeiou":
            vowels += 1
    return vowels