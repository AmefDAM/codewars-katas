def positive_sum(arr):
    sum = 0
    for number in arr:
        if number >= 0:
            sum += number
        else:
            sum += 0
    return sum