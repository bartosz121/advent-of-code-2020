data = [line.strip() for line in open("input.txt", 'r')]


def part1(code):
    """if return 0 - code finished by itself
    if return 1 - code in infinite loop"""

    position = 0
    visited = set()
    acc = 0
    while True:
        if position > len(code)-1:
            print(f"FINISHED | ACC -> {acc}")
            return 0
        instruction = code[position]
        op, arg = instruction.split(" ")
        if op == "jmp":
            position += int(arg)
        elif op == "acc":
            acc += int(arg)
            position += 1
        else:
            position += 1

        if position in visited:
            print(f"INF LOOP | ACC -> {acc}")
            return 1
        else:
            visited.add(position)


def part2():
    jmp_pos = [i for i, j in enumerate(data) if "jmp" in j]
    for pos in jmp_pos:
        code = data.copy()  # to avoid changing data in src
        code[pos] = "nop 2137"
        if part1(code) == 0:
            print("PART 2 SOLUTION FOUND")
            return 0
    # i guess i got lucky input bcs i tested it without a case where
    # 'nop is supposed to be a jmp' and i got a solution but if i wasnt, just
    # copy paste and change jmp to nop and it would work... i think


if __name__ == "__main__":
    # part1(data)
    part2()
