from enum import Enum

input = [line.strip() for line in open("input.txt", "r")]


class Directions(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

# part 1
# direction = [Directions(1)] # starting at E

# waypoint_directions[0] corresponds to waypoint_pos[0]; same for [1]
waypoint_directions = [Directions(1), Directions(0)]

# part 1
# pos = [0, 0]

ship_pos = [0, 0]
waypoint_pos = [10, 1]


def main():
    for instruction in input:
        # print(pos)
        action = instruction[0]
        units = int(instruction[1:])
        handle_instruction(action, units)
    # print(f"{pos=}") # part 1
    print(f"{ship_pos=}")
    print(abs(ship_pos[0])+abs(ship_pos[1]))

def handle_instruction(action: str, units: int):
    # print("======================")
    # print(f"\tWD: {waypoint_directions} WP: {waypoint_pos}")
    # print(f"\t {action=} {units=} {ship_pos=}")
    match action:
        case "N":
            waypoint_pos[1] += units
            if waypoint_pos[1] > 0:
                waypoint_directions[1] = Directions(0)
            # print(f"\t\t\t moved waypoint_pos {action} +{units} -> WP: {waypoint_pos}")
        case "S":
            waypoint_pos[1] -= units
            if waypoint_pos[1] < 0:
                waypoint_directions[1] = Directions(2)
            # print(f"\t\t\t moved waypoint_pos {action} -{units} -> WP: {waypoint_pos}")
        case "E":
            waypoint_pos[0] += units
            if waypoint_pos[0] > 0:
                waypoint_directions[0] = Directions(1)
            # print(f"\t\t\t moved waypoint_pos {action} +{units} -> WP: {waypoint_pos}")
        case "W":
            waypoint_pos[0] -= units
            if waypoint_pos[0] < 0:
                waypoint_directions[0] = Directions(3)
            # print(f"\t\t\t moved waypoint_pos {action} -{units} -> WP: {waypoint_pos}")
        case "L":
            turn_by = units//90
            waypoint_directions[0] = Directions((waypoint_directions[0].value - turn_by)%4)
            waypoint_directions[1] = Directions((waypoint_directions[1].value - turn_by)%4)
            rotate_direction(turn_by)
            post_rotation_check()
        case "R":
            turn_by = units//90
            waypoint_directions[0] = Directions((waypoint_directions[0].value + turn_by)%4)
            waypoint_directions[1] = Directions((waypoint_directions[1].value + turn_by)%4)
            rotate_direction(turn_by)
            post_rotation_check()

        case "F":
            # print(f"\t\t\t forward: ship_pos[0] += {waypoint_pos[0]*units} ship_pos[1] += {waypoint_pos[1]*units}")
            ship_pos[0] += waypoint_pos[0]*units
            ship_pos[1] += waypoint_pos[1]*units
            # handle_instruction(direction[0].name, units)


def rotate_direction(turns: int):
    for _ in range(turns):
        waypoint_pos[0], waypoint_pos[1] = waypoint_pos[1], waypoint_pos[0]

def post_rotation_check():
    """
    only for part2
    waypoint_directions[0] = east(+)/west(-)
    waypoint_directions[1] = north(+)/south(-)

    first check if directions are mixed up [0] should be east/west and swap if true

    then go over both directions and change symbol if needed
    """
    if waypoint_directions[0].value not in(1, 3):
        waypoint_directions[0], waypoint_directions[1] = waypoint_directions[1], waypoint_directions[0]

    # check symbols
    for direction in waypoint_directions:
        match direction.value:
            case 0:
                if waypoint_pos[1] < 0:
                    waypoint_pos[1] = abs(waypoint_pos[1])
            case 1:
                if waypoint_pos[0] < 0:
                    waypoint_pos[0] = abs(waypoint_pos[0])
            case 2:
                if waypoint_pos[1] > 0:
                    waypoint_pos[1] = -waypoint_pos[1]
            case 3:
                if waypoint_pos[0] > 0:
                    waypoint_pos[0] = -waypoint_pos[0]

# PART 1
# def handle_instruction(action: str, units: int):
#     # print(f"\t {action=} {units=} {direction[0].name=} {direction[0].value=}")
#     match action:
#         case "N":
#             pos[1] += units
#         case "S":
#             pos[1] -= units
#         case "E":
#             pos[0] += units
#         case "W":
#             pos[0] -= units
        # case "L":
        #     turn_by = direction[0].value - units//90
        #     direction[0] = Directions(turn_by % 4)
        # case "R":
        #     turn_by = direction[0].value + units//90
        #     direction[0] = Directions(turn_by % 4)
#         case "F":
#             handle_instruction(direction[0].name, units)


if __name__ == "__main__":
    main()
