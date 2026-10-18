def introverted_seat(seats: str) -> str | None:
    best_seat = None
    min_threats = 2

    for seat in range(len(seats)):
        if seats[seat] != "0":
            continue

        threats = 0

        if seat > 0 and seats[seat - 1] != " ":
            threats += 1

        if seat < len(seats) - 1 and seats[seat + 1] != " ":
            threats += 1

        if threats < min_threats:
            min_threats = threats
            best_seat = seat

    if best_seat is None:
        return None

    seats_list = list(seats)
    seats_list[best_seat] = "1"

    return "".join(seats_list)