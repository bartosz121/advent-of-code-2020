from collections import Counter

input_ = [line.strip().split(' ') for line in open("input.txt", "r")]
# test_case = [["1-3", "a:", "abcde"], ["1-3", "b:", "cdefg"], ["2-9", "c:", "ccccccccc"]]


def part1(inp):
    result_counter = 0

    for case in inp:
        min_, max_ = case[0].split('-')
        letter_counter = Counter(case[2])[case[1][0]]

        if int(min_) <= letter_counter <= int(max_):
            result_counter += 1

    return result_counter


def part2(inp):
    result_counter = 0

    for case in inp:
        pos1, pos2 = case[0].split('-')

        if (case[2][int(pos1)-1] == case[1][0]) ^ (case[2][int(pos2)-1] == case[1][0]):
            result_counter += 1

    return result_counter


if __name__ == '__main__':
    print(part1(input_))
    print(part2(input_))
