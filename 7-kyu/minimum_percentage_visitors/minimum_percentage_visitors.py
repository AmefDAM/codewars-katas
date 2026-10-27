def minimum_percentage(foods):
    items = 0
    accumulator = 0
    
    for item in foods:
        accumulator += item
        items += 1

    if (accumulator - (items - 1)*100) > 0:
        return (accumulator - (items - 1)*100)
    else:
        return 0