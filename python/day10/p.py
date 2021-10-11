data = [int(i.strip()) for i in open("input.txt", 'r')]
data2 = [int(i.strip()) for i in open("test.txt", 'r')]


def part1(src):
    sorted_data = sorted(src)
    jolts_diffs = {
        1: 0,
        2: 0,
        3: 0
    }
    i = 0
    while i < len(src):
        if i == len(src)-1:
            break
        # print(f"{sorted_data[i]}-{sorted_data[i + 1]})={sorted_data[i]-sorted_data[i+1]}")
        jolts_diffs[abs(sorted_data[i]-sorted_data[i+1])] += 1
        i += 1
    jolts_diffs[1] += 1
    jolts_diffs[3] += 1  # "Finally, your device's built-in adapter is always 3 higher than the highest adapter"
    print(jolts_diffs)
    print("PART 1 SOLUTION:", jolts_diffs[1]*jolts_diffs[3])


checked = {}
data = sorted(data)

data = [0] + data
data2.append(max(data)+3)
print(data)
def part2(pos):
    if pos == len(data) - 1:
        return 1

    if pos in checked:
        return checked[pos]

    total = 0
    for i in range(pos+1, len(data)):
        if data[i] - data[pos] <= 3:
            total += part2(i)

    print(f"pos:{pos} i range > len(data2)")
    checked[pos] = total
    print(checked)
    return total


if __name__ == "__main__":
    # part1(data2)
    print(part2(0))
    print(checked)
