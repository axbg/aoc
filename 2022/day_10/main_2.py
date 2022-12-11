def draw(cycles, prev_cycles, prev_value, drawing):
    real_pos = (prev_cycles + 1) % 40 - 1
    if real_pos == prev_value - 1 or real_pos == prev_value or real_pos == prev_value + 1:
        drawing += '#'
    else:
        drawing += '.'

    if cycles - prev_cycles == 2:
        curr_cycles = real_pos + 1
        if curr_cycles == prev_value - 1 or curr_cycles == prev_value or curr_cycles == prev_value + 1:
            drawing += '#'
        else:
            drawing += '.'

    return drawing


def main():
    noop = ('noop', 1)
    add = ('addx', 2)

    cycles = 0
    value = 1
    drawing = []

    for line in open('inp.txt', 'r'):
        line = line.strip().split(" ")

        prev_cycles = cycles
        prev_value = value

        if line[0] == noop[0]:
            cycles += noop[1]
        elif line[0] == add[0]:
            value += int(line[1])
            cycles += add[1]

        draw(cycles, prev_cycles, prev_value, drawing)

    # print drawing
    for i in range(0, 6):
        string = ''
        for j in range(0, 40):
            string += drawing[i * 40 + j]
        print(f"{string}")


if __name__ == "__main__":
    main()
