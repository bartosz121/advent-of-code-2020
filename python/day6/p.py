with open("input.txt", 'r') as f:
    # [:-1] to delete \n at the end because it messes up part2 intersection
    tmp = f.read()[:-1]

input_ = tmp.split("\n\n")


def day6(list_):
    part1 = 0
    part2 = 0
    start_group = 0
    for group in list_:
        answers = group.split("\n")

        # part 1
        part1 += len(set("".join(answers)))

        # part 2
        ans_sets = [set(ans) for ans in answers]
        # *ans_sets = unpacking
        part2 += len(ans_sets[0].intersection(*ans_sets))

    return part1, part2


if __name__ == '__main__':
    print(day6(input_))
