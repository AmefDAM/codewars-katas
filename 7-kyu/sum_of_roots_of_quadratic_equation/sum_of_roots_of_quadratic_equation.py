import math

def roots(a,b,c):
    discriminant = (b * b) - 4 * a * c
    if a != 0 and discriminant >= 0 : 
        x1 = (-b+ (math.sqrt((b * b) - 4 * a * c))) / (2 * a)
        x2 = (-b- (math.sqrt((b * b) - 4 * a * c))) / (2 * a)
        return round((x1 + x2), 2)
    if a != 0 and discriminant < 0:
        return None