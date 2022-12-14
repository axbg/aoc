def compare_lists(e1, e2):
    is_ok = None
    for e11, e22 in zip(e1, e2):
        result = compare_elements(e11, e22)

        if result == -1:
            is_ok = -1
            break

        if result == 1:
            is_ok = 1
            break

    if is_ok is None:
        if len(e1) > len(e2):
            is_ok = -1
        elif len(e2) > len(e1):
            is_ok = 1

    return is_ok


def compare_elements(e1, e2):
    if isinstance(e1, int) and isinstance(e2, int):
        if e1 > e2:
            return -1
        elif e1 == e2:
            return 0
        else:
            return 1
    elif isinstance(e1, list) and isinstance(e2, list):
        return compare_lists(e1, e2)
    elif (isinstance(e1, list) and isinstance(e2, int)) or \
            (isinstance(e1, int) and isinstance(e2, list)):
        e1 = e1 if isinstance(e1, list) else [e1]
        e2 = e2 if isinstance(e2, list) else [e2]
        return compare_lists(e1, e2)


def main():
    with open('inp.txt', 'r') as file:
        lines = file.readlines()

    counter = 0
    inp_index = 0
    for index in range(0, len(lines), 3):
        inp_index += 1
        line1 = eval(lines[index])
        line2 = eval(lines[index + 1])

        result = compare_lists(line1, line2)
        print(f"Pair {inp_index} is {result}")
        if result == 1:
            counter += inp_index

    print(f"Total result: {counter}")


if __name__ == "__main__":
    main()
