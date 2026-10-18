import string

def keyword_cipher(msg, keyword):
    real_keyword = ""
    
    alphabet = string.ascii_lowercase
    for letter in keyword:
        if letter not in set(real_keyword):
            real_keyword += letter
            alphabet = alphabet.replace(letter, "")
            
    complete_keyword = real_keyword + alphabet
    encrypted = ""
    
    for letter in msg.lower():
        if letter in string.ascii_lowercase:
            pos = string.ascii_lowercase.index(letter)
            encrypted += complete_keyword[pos]
        else:
            encrypted += letter
    return encrypted