def narcissistic(value):
    digits_list = [int(digit) for digit in str(value)]
    total = 0

    for digit in digits_list:
        total += digit ** len(digits_list)

    if total == value:
        return True

    return False