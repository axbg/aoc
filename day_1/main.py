def main():
    elves = []
    current = 0

    with open("inp.txt", "r") as file:
        for line in file:
            if line == '\n':
                elves.append(current)
                current = 0
            else:
                current += int(line)

    elves.sort(reverse=True)
    print(f"max is {elves[0]}")

    first_three = 0
    for i in range(0, 3):
        first_three += elves[i]

    print(f"the first three are carrying {first_three}")


if __name__ == "__main__":
    main()
