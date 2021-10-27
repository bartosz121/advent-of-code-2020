from collections import Counter, defaultdict
from itertools import product

input = [line.strip() for line in open("input.txt", "r")]


def int_to_bin(a: str) -> str:
    return format(int(a), "b")


def bin_to_int(a: str) -> int:
    return int(a, 2)


# part 1
# def main():
#     mem = defaultdict(int)
#     current_mask = ""

#     for line in input:
#         elements = line.split(" ")
#         if elements[0] == "mask":
#             current_mask = elements[-1]
#         else:
#             mem_address, _, value = elements
#             mem_address = mem_address[4:-1]
#             bin_value = int_to_bin(value)

#             # add leading zeroes to bin value to match mask
#             bin_value = list("0" * (36 - len(bin_value)) + bin_value)

#             for i, v in enumerate(current_mask):
#                 if v != "X":
#                     bin_value[i] = v

#             mem[mem_address] = bin_to_int("".join(bin_value))

#     print(sum(mem.values()))


def main():
    mem = defaultdict(int)
    current_mask = ""

    for line in input:
        elements = line.split(" ")
        if elements[0] == "mask":
            current_mask = elements[-1]
        else:
            mem_address, _, value = elements
            mem_address = mem_address[4:-1]
            bin_mem_addr = int_to_bin(mem_address)

            # add leading zeroes to bin value to match mask
            bin_mem_addr = list("0" * (36 - len(bin_mem_addr)) + bin_mem_addr)

            for i, v in enumerate(current_mask):
                if v in ("X", "1"):
                    bin_mem_addr[i] = v

            x_count = Counter("".join(bin_mem_addr))["X"]
            floating_bits = product("01", repeat=x_count)

            for bits in floating_bits:
                new_addr = list(bin_mem_addr)
                for i in range(x_count):
                    new_addr[new_addr.index("X")] = bits[i]

                mem[bin_to_int("".join(new_addr))] = int(value)

    print(f"{sum(mem.values())=}")


if __name__ == "__main__":
    main()
