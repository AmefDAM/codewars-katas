def sort_nested_list(lst):
    index = 0
    list_to_sort = []
    sorted_lst = []

    if isinstance(lst[0], int):
        return sorted(lst)

    elif isinstance(lst[0][0], int):
        for sublist in lst:
            list_to_sort += sublist

        list_to_sort.sort()

        for sublist in lst:
            new_sublist = []
            for item in sublist:
                new_sublist.append(list_to_sort[index])
                index += 1
            sorted_lst.append(new_sublist)
        return sorted_lst

    else:
        for sublist in lst:
            for item in sublist:
                list_to_sort += item

        list_to_sort.sort()

        for sublist in lst:
            new_sublist = []
            for sbsublist in sublist:
                new_sbsublist = []
                for item in sbsublist:
                    new_sbsublist.append(list_to_sort[index])
                    index += 1
                new_sublist.append(new_sbsublist)
            sorted_lst.append(new_sublist)
        return sorted_lst