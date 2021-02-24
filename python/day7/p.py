from collections import defaultdict

input_1 = [line.strip() for line in open("input.txt", 'r')]


def contains_bag(target):
    result = []
    for entry in input_1:
        if target in " ".join(entry.split()[3:]):
            result.append(" ".join(entry.split()[:2]))
    return result


def part1():
    # TODO FIX IT
    target1 = "shiny gold"
    returned = contains_bag(target1)
    returned_set = set(returned)
    while len(returned) != 0:
        for bag in returned:
            r = contains_bag(bag)
            returned.remove(bag)
            for b in r:
                returned.append(b)
                returned_set.add(b)
    counter = len(returned_set)
    print(counter)


def part2(color):
    rule = ''
    for line in input_1:
        if line[:line.index(" bags")] == color:
            rule = line

    if "no" in rule:
        return 1

    rule = rule.split("contain")[1].strip().split()

    result = 0
    i = 0
    while i < len(rule):
        count = int(rule[i])
        color = rule[i+1] + ' ' + rule[i+2]

        result += count * part2(color)
        i += 4

    return result + 1


if __name__ == '__main__':
    # print(input_1)
    # print(contains_bag("shiny gold"))
    # part1()
    print(part2("shiny gold")-1)
