def check_for_checkpoint(cycles, prev_cycles, value, prev_value, checkpoints):
    if cycles in checkpoints:
        print(f"Value during cycle {cycles} is {value}")
        return cycles * value
    else:
        for checkpoint in checkpoints:
            if prev_cycles < checkpoint < cycles:
                print(f"Value during cycle {checkpoint} is {prev_cycles}")
                return checkpoint * prev_value

    return 0


def main():
    noop = ('noop', 1)
    add = ('addx', 2)

    cycles = 1
    value = 1
    checkpoints = [20, 60, 100, 140, 180, 220]
    total_sum = 0
    for line in open('inp.txt', 'r'):
        line = line.strip().split(" ")

        prev_cycles = cycles
        prev_value = value

        if line[0] == noop[0]:
            cycles += noop[1]
        elif line[0] == add[0]:
            value += int(line[1])
            cycles += add[1]

        total_sum += check_for_checkpoint(cycles, prev_cycles, value, prev_value, checkpoints)

    print(total_sum)


if __name__ == "__main__":
    main()
