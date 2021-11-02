# input = [6, 4, 12, 1, 20, 0, 16]
input = [0, 3, 6]


def main():
    newest = {}
    history = {}
    occured_numbers = history.keys()
    turn_count = 1
    TARGET = 2020
    n = -1

    def handle_num_check():
        if n in newest:  # if true update newest turn
            history[n] = newest[n]
            newest[n] = turn_count
        else:
            newest[n] = turn_count  # add first occurence if not spoken before

    while turn_count <= TARGET:
        if turn_count <= len(input):  # add puzzle input
            n = input[turn_count - 1]
            newest[n] = turn_count
        else:
            if n in occured_numbers:
                # if n is in history -> it was spoken atleast two times
                n = newest[n] - history[n]
                handle_num_check()
            else:
                n = 0
                handle_num_check()

        turn_count += 1

    print(n)


if __name__ == "__main__":
    main()
