def solution(number):
    result = 0
    for x in range(0, number):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    return result