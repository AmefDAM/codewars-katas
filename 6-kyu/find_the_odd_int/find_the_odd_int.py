def find_it(seq):
    for number in set(seq):
        quantity = seq.count(number)
        
        if quantity % 2 != 0:
            return number