import re

def count_binary(s1, s2):
    return len(re.findall(f"(?={s1})", s2)) # f permite variables en string, (?= )lookahead positivo -"no gasta/excluye" caracteres encontrados-, len "cuenta"