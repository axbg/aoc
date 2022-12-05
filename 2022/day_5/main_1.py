def main():
    stacks = []

    with open("inp.txt", "r") as file:
        for line in file:
            if line.startswith(" ") or line.startswith("["):
                cols = "x" + line.replace("\n", "").replace(" ", "x") + "x"
                cols = cols.replace("xxxx", "X").replace("x", "").replace("[", "").replace("]", "")

                if cols[0] == '1':
                    continue

                if len(stacks) == 0:
                    stacks = [[] for i in range(0, len(cols))]

                for i in range(0, len(cols)):
                    if not stacks[i]:
                        stacks[i] = []

                    if cols[i] != 'X':
                        stacks[i].insert(0, cols[i])

            elif line.startswith("\n"):
                pass
            else:
                parsed = line.replace("\n", "").split(" ")
                no = int(parsed[1])
                start = int(parsed[3]) - 1
                target = int(parsed[5]) - 1

                for i in range(0, no):
                    stacks[target].append(stacks[start].pop())

        solution = ""
        for i in range(0, len(stacks)):
            solution += stacks[i][-1]
            print(f"On top of column {i + 1}: {stacks[i][-1]}")

        print(f"Solution is {solution}")


if __name__ == "__main__":
    main()
