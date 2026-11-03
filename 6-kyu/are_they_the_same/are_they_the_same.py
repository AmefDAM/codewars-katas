def comp(array1, array2):
    return array1 is not None and array2 is not None and sorted([abs(element) for element in array1]) == sorted([element ** 0.5 for element in array2])