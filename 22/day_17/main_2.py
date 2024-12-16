# Struggled a lot with this one, because I had a hard time imagining the cyclic pattern,
#   as I was using an infinite list, but did not use the original positions in order to detect actual matches
# Huge thanks to https://github.com/terminalmage/adventofcode/blob/main/2022/day17.py

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


def get_height(mapp):
    for x in range(0, len(mapp)):
        for y in range(0, len(mapp[x])):
            if mapp[x][y] == '#':
                return len(mapp) - x
    return 0

def compute_top_hash(mapp):
    top_lines = 9 if len(mapp) >= 9 else len(mapp)

    string = ''
    for i in range(0, top_lines):
        for j in range(0, len(mapp[i])):
            string += mapp[i][j]

    return string

def main():
    movements = cycle(enumerate((open('inp.txt', 'r').readlines()[0])))

    mapp = draw_map(4)
    blocks = cycle(enumerate(['horizontal_line', 'plus', 'l', 'vertical_line', 'square']))

    needed_blocks = 2022

    tracked = {}

    rock_index, rock_gen = next(blocks)
    block = Block(rock_gen)
    movement = 0
    for no_of_blocks in range(0, needed_blocks):
        generate_block = False

        while generate_block is False:
            movement += 1
            jet_index, direction = next(movements)

            # Even though it works for the challenge input, if the cycle is detected too early, test input will fail to validate,
            #   so we need to let some blocks arrange before starting to look for a cycle
            #       completely magical number that works for all the checks
            # Someone on reddit explained why this issue appears:
            #   In order for it to truly cycle, not only do the sequence of rocks and jets need to be the same,
            #   but the state of the top of the tower also needs to be the same. After a few cycles of the same
            #   sequence of rocks and jets, the top of the tower should be the same, but not necessarily in the
            #   first detection of the cycle if only the indexes of the rocks and the jets are considered.
            #   This may be why you say "if the cycle is small enough it won't be accurate".
            # I tried to implement this check, but it's still not working for the first input example and 2022 blocks,
            #   as, even with the new condition, the cycle is detected too early
            if no_of_blocks > 12:
                key = (rock_index, jet_index, compute_top_hash(mapp))

                if key in tracked:
                    prev_rock_num, elevation = tracked[key]
                    period = no_of_blocks - prev_rock_num

                    if no_of_blocks % period == needed_blocks % period:
                        print(
                            f'Cycle of period {period} detected '
                            f'(iterations {prev_rock_num} - {no_of_blocks})'
                        )
                        cycle_height = get_height(mapp) - elevation
                        rocks_remaining = needed_blocks - no_of_blocks
                        cycles_remaining = (rocks_remaining // period) + 1
                        print(f'Result is {elevation + (cycle_height * cycles_remaining)}')
                        return
                else:
                    tracked[key] = (no_of_blocks, get_height(mapp))

            apply_horizontal_movement(mapp, block, direction)
            generate_block = apply_fall(mapp, block)

        mapp = write_block_to_map(mapp, block)
        rock_index, rock_gen = next(blocks)
        block = Block(rock_gen)
        mapp = add_lines_to_map(mapp, block.height)

    print(f"Max height is {get_height(mapp)}")


if __name__ == "__main__":
    main()
