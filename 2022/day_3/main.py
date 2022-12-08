import string


def main():
    alphabet = list(string.ascii_letters)
    score = 0

    with open("inp.txt", "r") as file:
        for line in file:
            first = line[:len(line) // 2]
            second = line[len(line) // 2:]

            commons = list(set(first) & set(second))

            common_item = commons[0]
            score += (alphabet.index(common_item) + 1)

    print(f"the total score is {score}")


if __name__ == "__main__":
    main()
