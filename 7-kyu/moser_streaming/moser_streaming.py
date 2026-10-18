import itertools

def moser():
    for points in itertools.count(1, 1):
        yield (1 + (points * (points - 1)) / 2 + (points * (points - 1) * (points - 2) * (points - 3)) / 24)