def smart_log_formatter(logs):
    memory = []
    count = 0
    response = []
    for message in logs:
        if memory == []:
            memory = message
            count += 1
        elif message == memory:
            count += 1
        else:
            if count > 1:
                response.append(f"{memory} (x{count})")
            else:
                response.append(memory)
            memory = message
            count = 1

    if count > 1:
        response.append(f"{memory} (x{count})")
    elif memory == []:
        return response
    else:
        response.append(memory)

    return response