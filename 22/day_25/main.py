def get_numeric_value(number):
    if number == '-':
        number = '-1'
    elif number == '=':
        number = '-2'

    return int(number)


def transform_to_decimal(number):
    index = 0
    number = number[::-1]
    result = 0

    for numb in number:
        partial_result = int(get_numeric_value(numb) * pow(5, index))
        result += partial_result
        index += 1

    return result


def transform_to_snafu(number):
    if number == 4:
        return '-'
    elif number == 3:
        return '='
    else:
        return str(number)


def add_snafu(number, number1):
    snafu = []

    if len(number1) > len(number):
        aux = number
        number = number1[::-1]
        number1 = aux[::-1]
    else:
        number = number[::-1]
        number1 = number1[::-1]

    over = under = 0
    for i in range(0, len(number)):
        l = get_numeric_value(number[i])

        if len(number1) > i:
            ll = get_numeric_value(number1[i])
        else:
            ll = 0

        result = l + ll + over + under
        over = under = 0

        if result > 2:
            over = 1
        elif result < -2:
            under = -1

        snafu.append(transform_to_snafu(result % 5))

    if over == 1:
        snafu.append('1')

    snafu.reverse()
    return "".join(snafu)


def main():
    result = "0"

    numbers = open("inp.txt", "r").readlines()
    for number in numbers:
        result = add_snafu(result, number.strip())
        print(f"Partial result is {result} and in decimal {transform_to_decimal(result)}")

    print(f"Final result: {result}")


if __name__ == "__main__":
    main()
