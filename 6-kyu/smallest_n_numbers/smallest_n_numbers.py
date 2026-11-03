def first_n_smallest(number_list, n):

    if n == 0:
        return []

    ordered_list = sorted(number_list)[:n]
    result = []

    for number in number_list:
        if number in ordered_list:
            result.append(number)
            ordered_list.remove(number)

    return result