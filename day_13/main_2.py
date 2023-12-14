def extract_first_element(element):
    if isinstance(element, int):
        return element
    elif isinstance(element, list):
        if len(element) == 0:
            return 0
        else:
            return extract_first_element(element[0])


def main():
    with open('inp.txt', 'r') as file:
        lines = file.readlines()

    eval_lines = []
    for index in range(0, len(lines), 3):
        eval_lines.append(eval(lines[index]))
        eval_lines.append(eval(lines[index + 1]))

    eval_lines.append([2])
    eval_lines.append([6])

    extracted_lines = []
    for line in eval_lines:
        extracted_lines.append(extract_first_element(line))

    extracted_lines.sort()

    result = 1
    found_2 = False
    found_6 = False
    for index in range(0, len(extracted_lines)):
        if extracted_lines[index] == 2 and found_2 is False:
            found_2 = True
            print(f"Index {index + 1}: {extracted_lines[index]}")
            result *= (index + 1)

        if extracted_lines[index] == 6 and found_6 is False:
            found_6 = True
            print(f"Index {index + 1}: {extracted_lines[index]}")
            result *= (index + 1)

    print(f"Result is {result}")


if __name__ == "__main__":
    main()
