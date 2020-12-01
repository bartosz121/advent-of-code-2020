from itertools import combinations

input = [int(line.strip()) for line in open("input.txt", "r")]
# test_case1 = [1721, 979, 366, 299, 675, 1456]

TARGET = 2020


# def part1(list_):
#     for n1 in list_:
#         for n2 in list_:
#             if n1 + n2 == TARGET:
#                 print(n1, n2, n1*n2)
#                 return
#
#
# def part2(list_):
#     for n1 in list_:
#         for n2 in list_:
#             for n3 in list_:
#                 if n1 + n2 + n3 == TARGET:
#                     print(n1, n2, n3, n1 * n2 * n3)
#                     return


def part1(list_):
    for n1, n2 in combinations(list_, 2):
        if n1 + n2 == TARGET:
            print(n1, n2, n1*n2)
            return


def part2(list_):
    for n1, n2, n3 in combinations(list_, 3):
        if n1 + n2 + n3 == TARGET:
            print(n1, n2, n3, n1*n2*n3)
            return


if __name__ == '__main__':
    part1(input)
    part2(input)

