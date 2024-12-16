import string


def main():
    alphabet = list(string.ascii_letters)
    score = 0

    with open("inp.txt", "r") as file:
        counter = 0
        groups = []

        for line in file:
            counter += 1
            groups.append(line.strip())

            if counter == 3:
                common_list = list(set(groups[0]) & set(groups[1]) & set(groups[2]))
                common_item = common_list[0]
                score += (alphabet.index(common_item) + 1)
                groups = []
                counter = 0

    print(f"the total score is {score}")


if __name__ == "__main__":
    main()
