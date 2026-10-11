def spin_words(sentence):
    result = ""
    words = sentence.split(" ")
    
    for word in words:
        if len(word)<5:
            result += word + " "
        else:
            result += word[::-1] + " "
    
    
    return result.rstrip()