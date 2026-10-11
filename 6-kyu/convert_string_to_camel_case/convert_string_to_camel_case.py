def to_camel_case(text):
    import re
    words = re.split(r'[-_]', text)
    
    result = words[0] + "".join(word.title() for word in words[1:])
    
    return result