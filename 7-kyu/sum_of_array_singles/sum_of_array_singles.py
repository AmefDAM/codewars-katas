def repeats(arr):
    total = 0
    for x in arr:
        if arr.count(x) == 1:
            total += x
    return total