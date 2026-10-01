def multi_table(number):
    table = ""
    multiplo = 1
    while multiplo < 11:
        if multiplo < 10:
            table += f"{multiplo} * {number} = {multiplo * number}\n"
        else:
            table += f"{multiplo} * {number} = {multiplo * number}"
        multiplo += 1
    return table