from itertools import combinations

data = [int(line.strip()) for line in open("input.txt", 'r')]


def workworkwork(preambleN, data_src):
    n = preambleN
    while n < len(data_src):
        preamble = data_src[n-preambleN:n+1]  # n+1 bcs how slicing works, I need one more element
        preamble_sums = set(i+j for i, j in combinations(preamble, 2))
        try:
            if data_src[n+1] not in preamble_sums:
                print(f"PART 1 SOLUTION: {data_src[n+1]}")
                target = data_src[n+1]
                # PART 2 HERE
                # TODO not really efficient refactor later
                k = 3
                i = k
                j = 0
                while True:
                    if k > len(data_src):
                        break
                    # print(f"{j}:{i} | {data_src[j:i]} {sum(data_src[j:i])}")
                    if i > len(data_src):
                        k += 1
                        i = k
                        j = 0
                        continue
                    if sum(data_src[j:i]) == target:
                        dupa123 = data_src[j:i]
                        print(f"PART 2 SOLUTION FOUND: {dupa123}\n\tMIN+MAX:{min(dupa123)+max(dupa123)}")
                        break
                    else:
                        i += 1
                        j += 1

        except IndexError:
            pass
        n += 1


if __name__ == "__main__":
    workworkwork(25, data)
