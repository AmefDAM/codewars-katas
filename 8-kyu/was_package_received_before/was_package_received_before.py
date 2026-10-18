def was_package_received_yesterday(tz_from, tz_to, start, duration):
    difference = tz_to - tz_from
    day = 0
    arrival_time = 0
    if start + duration >= 24:
        arrival_time = (start + duration) - 24
        day += 1
    else:
        arrival_time = start + duration
    if arrival_time + difference < 0:
        arrival_time = arrival_time + difference + 24
        day -= 1
    elif arrival_time + difference >= 24:
        arrival_time = arrival_time + difference - 24
        day += 1
    return day == -1