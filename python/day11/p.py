import copy
from collections import Counter
from itertools import chain
from typing import List

DUMMY_CHAR = "/"
FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"

# wrap layout around with dummy chars to make life easier later on
input = [list(DUMMY_CHAR+line.strip()+DUMMY_CHAR) for line in open("input.txt", "r")]

# wrapping up and down
row_length = len(input[0])
input.insert(0, [*DUMMY_CHAR * row_length])
input.append([*DUMMY_CHAR * row_length])


# PART 1
# def count_seats(seat_layout: List[List[str]], seat_y: int, seat_x: int) -> int:
#     adjacent_occupied_seats = 0
#     # N
#     if seat_layout[seat_y - 1][seat_x] == OCCUPIED_SEAT:
#         adjacent_occupied_seats += 1
#     # NE
#     if seat_layout[seat_y - 1][seat_x + 1] == OCCUPIED_SEAT:
#         adjacent_occupied_seats += 1
#     # E
#     if seat_layout[seat_y][seat_x + 1] == OCCUPIED_SEAT:
#         adjacent_occupied_seats += 1
#     # SE
#     if seat_layout[seat_y + 1][seat_x + 1] == OCCUPIED_SEAT:
#         adjacent_occupied_seats += 1
#     # S
#     if seat_layout[seat_y + 1][seat_x] == OCCUPIED_SEAT:
#         adjacent_occupied_seats += 1
#     # SW
#     if seat_layout[seat_y + 1][seat_x - 1] == OCCUPIED_SEAT:
#         adjacent_occupied_seats += 1
#     # W
#     if seat_layout[seat_y][seat_x - 1] == OCCUPIED_SEAT:
#         adjacent_occupied_seats += 1
#     # NW
#     if seat_layout[seat_y - 1][seat_x - 1] == OCCUPIED_SEAT:
#         adjacent_occupied_seats += 1
#     return adjacent_occupied_seats


def check_seat_in_direction(seat_layout: List[List[str]], direction: str, seat_y: int, seat_x: int) -> int:
    # print(f"seat[{seat_y}][{seat_x}] {direction} -> ", end="")
    match direction:
        case 'N':
            candidate = seat_layout[seat_y - 1][seat_x]
            seat_y -= 1
        case 'NE':
            candidate = seat_layout[seat_y - 1][seat_x + 1]
            seat_y -= 1
            seat_x += 1
        case 'E':
            candidate = seat_layout[seat_y][seat_x + 1]
            seat_x += 1
        case 'SE':
            candidate = seat_layout[seat_y + 1][seat_x + 1]
            seat_y += 1
            seat_x += 1
        case 'S':
            candidate = seat_layout[seat_y + 1][seat_x]
            seat_y += 1
        case 'SW':
            candidate = seat_layout[seat_y + 1][seat_x - 1]
            seat_y += 1
            seat_x -= 1
        case 'W':
            candidate = seat_layout[seat_y][seat_x - 1]
            seat_x -= 1
        case 'NW':
            candidate = seat_layout[seat_y - 1][seat_x - 1]
            seat_y -= 1
            seat_x -= 1

    # print(f"candidate: '{candidate}' -> ", end="")

    if candidate == OCCUPIED_SEAT:
        # print("OCCUPIED -> +1")
        return 1
    if candidate == FLOOR:
        # print(f"EMPTY SEAT CHECKING NEXT")
        return check_seat_in_direction(seat_layout, direction, seat_y, seat_x)

    # print("EMPTY OR DUMMY -> 0")
    return 0


# PART 1
# def simulate(not_working_layout: List[List[str]]) -> List[List[str]]:
#     working_input = copy.deepcopy(not_working_layout)
#     for y, seat_row in enumerate(not_working_layout):
#         for x, seat in enumerate(seat_row):
#             if seat == DUMMY_CHAR:
#                 continue
#             occupied_seats = count_seats(not_working_layout, y, x)
#             # print(f"seat[{y}][{x}]: {seat} occupied_seats: {occupied_seats}")
#             match seat:
#                 case 'L':
#                     if occupied_seats == 0:
#                         # print(f"not_working_layout[{y}][{x}]: {not_working_layout[y][x]}", end=" ")
#                         working_input[y][x] = OCCUPIED_SEAT
#                         # print(f"converted to {working_input[y][x]}")
#                 case '#':
#                     if occupied_seats >= 4:
#                         # print(f"not_working_layout[{y}][{x}]: {not_working_layout[y][x]}", end=" ")
#                         working_input[y][x] = EMPTY_SEAT
#                         # print(f"converted to {working_input[y][x]}")

#     return working_input

def simulate(not_working_layout: List[List[str]]) -> List[List[str]]:
    working_input = copy.deepcopy(not_working_layout)
    for y, seat_row in enumerate(not_working_layout):
        for x, seat in enumerate(seat_row):
            if seat == DUMMY_CHAR:
                continue
            occupied_seats = 0
            # print("=======================")
            for direction in ("N", "NE", "E", "SE", "S", "SW", "W", "NW"):
                occupied_seats += check_seat_in_direction(not_working_layout, direction, y, x)
            # print(f"RESULT: {occupied_seats}")
            # print("=======================")
            # print(f"seat[{y}][{x}]: {seat} occupied_seats: {occupied_seats}")
            match seat:
                case 'L':
                    if occupied_seats == 0:
                        working_input[y][x] = OCCUPIED_SEAT
                case '#':
                    if occupied_seats >= 5:
                        working_input[y][x] = EMPTY_SEAT

    return working_input

def count_all_occupied_seats(layout: List[List[str]]) -> int:
    return Counter(chain(*layout))[OCCUPIED_SEAT]


if __name__ == "__main__":
    x = simulate(input)

    while True:
        old = count_all_occupied_seats(x)
        x = simulate(x)
        new = count_all_occupied_seats(x)
        if old == new:
            print(new)
            break
