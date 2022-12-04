def main():
    score = 0

    with open("inp.txt", "r") as file:
        for line in file:
            [first, second] = line.strip().split(",")

            [first_left, first_right] = first.split("-")
            [second_left, second_right] = second.split("-")

            first_left = int(first_left)
            first_right = int(first_right)
            second_left = int(second_left)
            second_right = int(second_right)

            if (second_left >= first_left and second_right <= first_right) \
                    or (first_left >= second_left and first_right <= second_right):
                score += 1

    print(f"the total score is {score}")


if __name__ == "__main__":
    main()
