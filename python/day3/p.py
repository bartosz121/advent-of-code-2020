input_ = [line.strip() for line in open("input.txt", "r")]
# input_test = [line.strip() for line in open("test_case.txt", "r")]


def toboggan(map_, slope):
    current_x = 0
    current_y = 0
    x_slope = slope[0]
    y_slope = slope[1]
    pattern_len = len(map_[0])
    end_y = len(map_)-1
    trees_counter = 0

    while current_y <= end_y:
        # print(f"x:{current_x} y:{current_y} = {map_[current_y][current_x]}")
        if map_[current_y][current_x] == '#':
            trees_counter += 1

        current_x = (current_x + x_slope) % pattern_len
        current_y += y_slope

    return trees_counter


if __name__ == '__main__':
    print("Part 1", toboggan(input_, slope=(3, 1)), sep=": ")

    # xD
    print("Part 2", toboggan(input_, slope=(1, 1))*toboggan(input_, slope=(3, 1))
          *toboggan(input_, slope=(5, 1))*toboggan(input_, slope=(7, 1))
          *toboggan(input_, slope=(1, 2)), sep=": ")
