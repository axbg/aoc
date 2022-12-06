def main():
    # challenge 1
    limit = 4

    # challenge 2
    limit = 14

    with open("inp.txt", "r") as file:
        input = list(file.readlines()[0])

        dl = list()
        for i in range(0, limit):
            dl.append(input[i])

        ds = set(dl)
        if len(ds) == limit:
            print(4)

        for i in range(limit, len(input)):
            del dl[0]
            dl.append(input[i])
            ds = set(dl)

            if len(ds) == limit:
                print(i + 1)
                break


if __name__ == "__main__":
    main()
