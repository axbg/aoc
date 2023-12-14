from copy import deepcopy
from itertools import cycle


class Block:
    def __init__(self, typ):
        self.typ = typ
        self.height = 0
        self.coordinates = []
        self.generate_coordinates()

    def generate_coordinates(self):
        if self.typ == 'horizontal_line':
            self.coordinates.append((0, 2))
            self.coordinates.append((0, 3))
            self.coordinates.append((0, 4))
            self.coordinates.append((0, 5))
            self.height = 1
        elif self.typ == 'vertical_line':
            self.coordinates.append((0, 2))
            self.coordinates.append((1, 2))
            self.coordinates.append((2, 2))
            self.coordinates.append((3, 2))
            self.height = 4
        elif self.typ == 'plus':
            self.coordinates.append((0, 3))
            self.coordinates.append((1, 2))
            self.coordinates.append((1, 3))
            self.coordinates.append((1, 4))
            self.coordinates.append((2, 3))
            self.height = 3
        elif self.typ == 'square':
            self.coordinates.append((0, 2))
            self.coordinates.append((0, 3))
            self.coordinates.append((1, 2))
            self.coordinates.append((1, 3))
            self.height = 2
        elif self.typ == 'l':
            self.coordinates.append((0, 4))
            self.coordinates.append((1, 4))
            self.coordinates.append((2, 2))
            self.coordinates.append((2, 3))
            self.coordinates.append((2, 4))
            self.height = 3

    def apply_horizontal_movement(self, movement):
        value = 1 if movement == '>' else -1
        new_coords = []
        for coordinate in self.coordinates:
            new_coords.append((coordinate[0], coordinate[1] + value))

        self.coordinates = new_coords

    def apply_fall(self):
        new_coords = []
        for coordinate in self.coordinates:
            new_coords.append((coordinate[0] + 1, coordinate[1]))

        self.coordinates = new_coords


def draw_map(lines):
    return [['.' for _ in range(0, 7)] for _ in range(0, lines)]


def add_lines_to_map(mapp, block_height):
    needed_lines = block_height + 3

    latest_line_with_element = len(mapp) - 1
    cont = True
    for x in range(0, len(mapp)):
        if cont:
            for j in range(0, len(mapp[x])):
                if mapp[x][j] == '#':
                    latest_line_with_element = x
                    cont = False
                    break

    if needed_lines >= latest_line_with_element:
        lines = needed_lines - latest_line_with_element
        for _ in range(0, lines):
            mapp.insert(0, ['.' for _ in range(0, 7)])
    else:
        lines = latest_line_with_element - needed_lines
        for _ in range(0, lines):
            mapp.pop(0)

    return mapp


def print_map(mapp):
    for x in range(0, len(mapp)):
        line = ''
        for y in range(0, len(mapp[x])):
            line += mapp[x][y]
        print(line)
    print('')


def print_block_on_map(mapp, block):
    mapp2 = deepcopy(mapp)

    for coordinate in block.coordinates:
        mapp2[coordinate[0]][coordinate[1]] = '@'
    print_map(mapp2)


def write_block_to_map(mapp, block):
    for coordinate in block.coordinates:
        mapp[coordinate[0]][coordinate[1]] = '#'

    return mapp


def apply_horizontal_movement(mapp, block, movement):
    if movement == '>':
        is_valid = True
        for coordinate in block.coordinates:
            if coordinate[1] == 6:
                is_valid = False
                break

            if mapp[coordinate[0]][coordinate[1] + 1] != '.':
                is_valid = False
                break
    else:
        is_valid = True
        for coordinate in block.coordinates:
            if coordinate[1] == 0:
                is_valid = False
                break

            if mapp[coordinate[0]][coordinate[1] - 1] != '.':
                is_valid = False
                break

    if is_valid:
        block.apply_horizontal_movement(movement)


def apply_fall(mapp, block):
    is_valid = True
    for coordinate in block.coordinates:
        if coordinate[0] == len(mapp) - 1:
            is_valid = False
            break

        if mapp[coordinate[0] + 1][coordinate[1]] != '.':
            is_valid = False
            break

    if is_valid:
        block.apply_fall()

    return not is_valid


def main():
    movements = cycle((open('inp.txt', 'r').readlines()[0]))

    mapp = draw_map(4)
    blocks = cycle(['horizontal_line', 'plus', 'l', 'vertical_line', 'square'])

    generate_block = False
    block = Block(next(blocks))
    no_of_blocks = 0
    for movement in movements:
        if generate_block:
            if no_of_blocks == 2022:
                for x in range(0, len(mapp)):
                    for y in range(0, len(mapp[x])):
                        if mapp[x][y] == '#':
                            print(f"Max height is {len(mapp) - x}")
                            exit()

            mapp = write_block_to_map(mapp, block)
            block = Block(next(blocks))
            mapp = add_lines_to_map(mapp, block.height)
            no_of_blocks += 1

        apply_horizontal_movement(mapp, block, movement)
        generate_block = apply_fall(mapp, block)


if __name__ == "__main__":
    main()
