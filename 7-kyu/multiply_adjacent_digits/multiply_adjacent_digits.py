import re

def digit_multiplication(expression):
    numbers = re.findall(r'\d+', expression)
    operators = re.findall(r'[-+]', expression)
    results = []
    for number in numbers:
        result = 1
        for digit in number:
            result *= int(digit)
        results.append(result)
    total = results[0]
    for index in range(len(operators)):
        if operators[index] == "+":
            total += results[index + 1]
        else:
            total -= results[index + 1]

    return total