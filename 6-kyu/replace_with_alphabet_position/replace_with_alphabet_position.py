import string


def alphabet_position(text):
    transcription = ""

    for character in text.lower():
        if character.isalpha():
            transcription += str(string.ascii_lowercase.index(character) + 1) + " "

    return transcription.rstrip()