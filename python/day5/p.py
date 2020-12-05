def boarding():
    seats = []
    max_seatid = 0

    for ticket in open("input.txt", "r"):
        ticket = ticket.strip()
        row = [0, 127]
        for dir_row in ticket[:7]:
            if dir_row == "F":
                row[1] = (row[0]+row[1])//2
            elif dir_row == "B":
                row[0] = (row[0]+row[1])//2

        column = [0, 7]
        for dir_col in ticket[7:]:
            if dir_col == "L":
                column[1] = (column[0]+column[1])//2
            elif dir_col == "R":
                column[0] = (column[0]+column[1])//2

        row = row[1]
        column = column[1]
        seat_id = row * 8 + column
        seats.append(seat_id)

        if seat_id > max_seatid:
            max_seatid = seat_id

    # part 2
    seats = sorted(seats)
    seq = set(range(seats[0], seats[-1]))
    my_seat = seq.difference(set(seats))

    return max_seatid, my_seat


if __name__ == '__main__':
    print(boarding())
