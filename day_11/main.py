from math import floor


def compute(item, value):
    return item if value == 'old' else int(value)


def throw_item(item, monkey, monkeys):
    monkeys[int(monkey)].append_item(item)


class Monkey:
    def __init__(self, name, items, op, test, test_true, test_false):
        self.name = name
        self.items = [int(x) for x in items]
        self.items_inspected = 0
        self.op = op
        self.test = test
        self.test_true = test_true
        self.test_false = test_false

    def __str__(self):
        return f"{self.name} ## {self.items} ## {self.op} ## {self.test} ## {self.test_true} ## {self.test_false}"

    def append_item(self, item):
        self.items.append(item)

    def get_name(self):
        return self.name

    def get_items_inspected(self):
        return self.items_inspected

    def inspect_items(self, monkeys):
        while len(self.items) != 0:
            self.items_inspected += 1
            self.compute_condition(self.apply_operation(self.items.pop(0)), monkeys)

    def apply_operation(self, item):
        operation = self.op.split(" ")

        if operation[1] == '+':
            item = item + compute(item, operation[2])
        elif operation[1] == '*':
            item = item * compute(item, operation[2])

        return floor(int(item) / 3)

    def compute_condition(self, item, monkeys):
        if (item % int(self.test)) == 0:
            throw_item(item, int(self.test_true), monkeys)
        else:
            throw_item(item, int(self.test_false), monkeys)


def main():
    monkeys = []

    file = open('inp.txt', 'r')
    data = file.readlines()

    i = 0
    while i < len(data):
        name = data[i].strip().split(" ")[1].split(":")[0]
        items = data[i + 1].split(":")[1].strip().split(', ')
        op = data[i + 2].split("=")[1].strip()
        test = data[i + 3].split("by")[1].strip()
        test_true = data[i + 4].strip().split(" ")[-1]
        test_false = data[i + 5].strip().split(" ")[-1]

        monkeys.append(Monkey(name, items, op, test, test_true, test_false))
        i += 7

    rounds = 20
    for _ in range(0, rounds):
        for monkey in monkeys:
            monkey.inspect_items(monkeys)

    monkeys.sort(key=lambda x: x.get_items_inspected(), reverse=True)

    for monkey in monkeys:
        print(f"Monkey {monkey.get_name()} inspected {monkey.get_items_inspected()} items")

    print(f"Monkey business score is {monkeys[0].get_items_inspected() * monkeys[1].get_items_inspected()}")


if __name__ == "__main__":
    main()
