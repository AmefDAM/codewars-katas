def find_uniq(xs):
    numbers = set(xs)
    for number in set(xs):
        if xs.count(number) == 1:
            return number