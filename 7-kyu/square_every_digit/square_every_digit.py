def square_digits(num):
    result = ""
    for digit in str(num):
        result += str(int(digit) * int(digit))
    return int(result)