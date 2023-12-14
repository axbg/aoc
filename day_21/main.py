def solve_monkey(monkey_name, monkeys):
    monkey = monkeys[monkey_name]

    if monkey['result']:
        return monkey['result']

    [monkey1, operation, monkey2] = monkey['operation'].split(" ")

    monkey1 = solve_monkey(monkey1, monkeys)
    monkey2 = solve_monkey(monkey2, monkeys)

    if operation == '+':
        return monkey1 + monkey2
    elif operation == '-':
        return monkey1 - monkey2
    elif operation == '*':
        return monkey1 * monkey2
    elif operation == '/':
        return monkey1 / monkey2


def main():
    monkeys = {}
    for line in open("inp.txt", "r"):
        line = line.strip()

        [current_monkey, operation] = line.split(":")
        operation = operation.strip()

        if operation.isnumeric():
            result = int(operation)
            operation = ''
        else:
            result = None

        monkeys[current_monkey] = {'name': current_monkey, 'operation': operation, 'result': result}

    print(f"Root monkey says {solve_monkey('root', monkeys)}")


if __name__ == "__main__":
    main()
