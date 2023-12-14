from copy import deepcopy

FACING_RIGHT = 0
FACING_DOWN = 1
FACING_LEFT = 2
FACING_UP = 3


def get_direction_symbol(direction):
    if direction == FACING_RIGHT:
        return '>'
    elif direction == FACING_LEFT:
        return '<'
    elif direction == FACING_UP:
        return '^'
    elif direction == FACING_DOWN:
        return 'v'


def compute_map(lines):
    length = 0
    height = 0
    for line in lines:
        if line == '\n':
            break

        height += 1
        if '.' in line and len(line) > length:
            length = len(line)

    ct = 0
    mapp = [[] for x in range(0, height)]
    for line in lines:
        if line == '\n':
            break

        line = line.replace('\n', '').replace(' ', '~')
        for j in range(0, len(line)):
            mapp[ct].append(line[j])

        for r in range(len(line), length - 1):
            mapp[ct].append('~')
        ct += 1

    return mapp


def compute_instructions(lines):
    line = lines[-1]

    instructions = []

    str = ''
    for element in line:
        if element.isnumeric():
            str += element
        else:
            instructions.append(int(str))
            instructions.append(element)
            str = ''

    if str.isnumeric():
        instructions.append(int(str))
    else:
        instructions.append(str)

    return instructions


def print_map(map):
    for i in range(0, len(map)):
        row = ''
        for j in range(0, len(map[i])):
            row += map[i][j]
        print(row)


def get_first_position(mapp):
    for i in range(0, len(mapp)):
        for j in range(0, len(mapp[i])):
            if mapp[i][j] == '.':
                return i, j, FACING_RIGHT


def navigate(mapp, instructions, position):
    x = position[0]
    y = position[1]
    f = position[2]

    for instruction in instructions:
        if str(instruction).isnumeric():
            [x, y, f] = move_on_map(mapp, (x, y, f), instruction, 'N')
        else:
            [x, y, f] = move_on_map(mapp, (x, y, f), 0, instruction)

        # print_on_map(mapp, x, y, f)

    return x, y, f


def get_rotation(f):
    if f == FACING_RIGHT:
        line_direction = 1
        column_direction = 0
    elif f == FACING_LEFT:
        line_direction = -1
        column_direction = 0
    elif f == FACING_UP:
        line_direction = 0
        column_direction = -1
    else:
        line_direction = 0
        column_direction = 1

    return line_direction, column_direction


def move_on_map(mapp, coordinates, distance, direction):
    [x, y, f] = coordinates

    if direction == 'R':
        f = (f + 1) % 4
    elif direction == 'L':
        f = (f - 1) % 4

    line_direction, column_direction = get_rotation(f)

    for step in range(0, distance):
        new_x = (x + column_direction) % len(mapp)
        new_y = (y + line_direction) % len(mapp[0])

        while mapp[new_x][new_y] == '~':
            new_x = (new_x + column_direction) % len(mapp)
            new_y = (new_y + line_direction) % len(mapp[0])

        if mapp[new_x][new_y] == '.':
            x = new_x
            y = new_y
        elif mapp[new_x][new_y] == '#':
            break

    return x, y, f


def print_on_map(mapp, x, y, f):
    mappp = deepcopy(mapp)
    mappp[x][y] = get_direction_symbol(f)
    print_map(mappp)
    print("\n")


def main():
    lines = open('inp.txt', 'r').readlines()

    mapp = compute_map(lines)
    instructions = compute_instructions(lines)

    # print_on_map(mapp, *get_first_position(mapp))

    [row, column, facing] = navigate(mapp, instructions, get_first_position(mapp))

    print(f"Solution is {((row + 1) * 1000) + ((column + 1) * 4) + facing}")


if __name__ == "__main__":
    main()
