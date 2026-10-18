import re

def remove_noise(st):
    noise = r"[%$&/#·@|º\\ª]"
    
    return re.sub(noise, "", st)