input = [6, 4, 12, 1, 20, 0, 16]
# input = [0, 3, 6]


def main():
    newest = {}
    history = {}
    occured_numbers = history.keys()
    turn_count = 1
    TARGET = 30000000
    n = -1

    def handle_num_check():
        """Checks if number was 'spoken' before"""
        if n in newest:
            history[n] = newest[n]
            newest[n] = turn_count
        else:
            newest[n] = turn_count

    while turn_count <= TARGET:
        if turn_count <= len(input):  # add puzzle input
            n = input[turn_count - 1]
            newest[n] = turn_count
        else:
            if n in occured_numbers:
                n = newest[n] - history[n]
                handle_num_check()
            else:
                n = 0
                handle_num_check()

        turn_count += 1

    print(n)


if __name__ == "__main__":
    main()
