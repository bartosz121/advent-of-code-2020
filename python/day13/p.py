from functools import reduce

input = [line.strip() for line in open("input.txt")]


# part 1
# def main():
#     earliest_ts = int(input[0])
#     bus_ids = tuple(filter(lambda c: c != "x", input[1:][0].split(",")))

#     found = False
#     time = earliest_ts
#     while found is False:
#         print(time)
#         for bus_id in bus_ids:
#             if time % int(bus_id) == 0:
#                 print(f"{bus_id=} | {(time - earliest_ts) * int(bus_id)=}")
#                 found = True
#                 break
#         time += 1

# part 2 functions below
def chinese_remainder(nums, rems):
    """https://shainer.github.io/crypto/math/2017/10/22/chinese-remainder-theorem.html"""
    result = 0
    prod = reduce((lambda x, y: x * y), nums)
    pp = [prod // n for n in nums]
    inv = [modInverse(pp[i], nums[i]) for i in range(len(nums))]

    for i in range(len(nums)):
        result += rems[i] * pp[i] * inv[i]

    return result % prod


def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1


def main():
    bus_ids = input[1].split(",")
    nums, rems = [], []

    for i, bus in enumerate(bus_ids):
        try:
            bus = int(bus)
            nums.append(bus)
            rems.append(bus - i)
        except ValueError:
            continue

    rems[0] = 0
    print(chinese_remainder(nums, rems))


if __name__ == "__main__":
    main()
