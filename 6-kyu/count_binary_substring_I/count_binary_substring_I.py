import re

def count_binary(s1, s2):
    return len(re.findall(f"(?={s1})", s2))