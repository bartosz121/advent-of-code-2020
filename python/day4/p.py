import re

input_ = [line.strip() for line in open("input.txt", "r")]


def part2_check(passport):
    patterns = {
        "byr": r"(^(19)[2-9][0-9]$)|((200)[0-2]$)",
        "iyr": r"(^(201)[0-9]$)|(^(2020)$)",
        "eyr": r"(^(202)[0-9]$)|(^(2030)$)",
        "hgt": r"(^(1[5-8][0-9]|19[0-3])cm$|(^([5-6])[0-9]|(^7)[0-6])in$)",
        "hcl": r"^(#)([a-f0-9]{6}$)",
        "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"^([0-9]{9})$"
    }

    valid = True
    for key in patterns.keys():
        valid = valid and bool(re.match(patterns[key], passport[key]))

    if valid:
        return True
    return False


def passport_check(list_):
    valid_passports_p1 = 0
    valid_passports_p2 = 0
    fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
    i_passport_start = 0

    # work on each passport 'on the fly' no need to save them to list or smth
    for i, v in enumerate(list_):
        if v == "" or i == len(list_)-1:
            # for last passport
            if i == len(list_)-1:
                passport = " ".join(list_[i_passport_start:]) \
                    .strip().split(" ")
            else:
                passport = " ".join(list_[i_passport_start:i])\
                    .strip().split(" ")

            passport_dict = {field: "N/A" for field in fields}

            for field in map(lambda f: f.split(":"), passport):
                # field[0] = field name, field[1] = field value
                passport_dict[field[0]] = field[1]

            # Part 1
            valid = True
            for field in fields:
                if field == "cid":
                    continue
                valid = valid and passport_dict[field] != "N/A"

            if valid:
                valid_passports_p1 += 1

            # Part 2
            if part2_check(passport_dict):
                valid_passports_p2 += 1

            i_passport_start = i

    return valid_passports_p1, valid_passports_p2


if __name__ == '__main__':
    print(passport_check(input_))
