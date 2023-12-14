from string import ascii_lowercase

alphabet = list(ascii_lowercase)


class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level

    def __str__(self):
        return f"{self.x}:{self.y}"


def replace_checkpoints(value):
    new_val = value
    if value == 'S':
        new_val = alphabet.index('a')
    elif value == 'E':
        new_val = alphabet.index('z')

    return int(new_val)


def apply_check(node, end, summits):
    current = replace_checkpoints(summits[node.x][node.y])
    next_current = replace_checkpoints(summits[end[0]][end[1]])

    return next_current - current <= 1 or current > next_current


def check_visited(current, visited):
    for node in visited:
        if current.x == node.x and current.y == node.y:
            return True

    return False


def bfs(summits, visited, start, end):
    check_nodes = [Node(start[0], start[1], 0)]

    while len(check_nodes) != 0:
        node = check_nodes.pop(0)

        if check_visited(node, visited):
            continue

        visited.add(node)
        print(f"Checking node {node.x}:{node.y} on level {node.level}")

        if node.x == end[0] and node.y == end[1]:
            print(f"reached end: {node.level}")
            break

        # up
        if node.x > 0 and check_visited(Node(node.x - 1, node.y, 0), visited) is False and apply_check(node, (
                node.x - 1, node.y), summits):
            check_nodes.append(Node(node.x - 1, node.y, node.level + 1))
        # right
        if node.y < len(summits[0]) - 1 and check_visited(Node(node.x, node.y + 1, 0),
                                                          visited) is False and apply_check(node,
                                                                                            (node.x, node.y + 1),
                                                                                            summits):
            check_nodes.append(Node(node.x, node.y + 1, node.level + 1))
        # down
        if node.x < len(summits) - 1 and check_visited(Node(node.x + 1, node.y, 0), visited) is False and apply_check(
                node, (node.x + 1, node.y),
                summits):
            check_nodes.append(Node(node.x + 1, node.y, node.level + 1))
        # left
        if node.y > 0 and check_visited(Node(node.x, node.y - 1, 0), visited) is False and apply_check(node, (
                node.x, node.y - 1), summits):
            check_nodes.append(Node(node.x, node.y - 1, node.level + 1))


def print_solution(solution, point, movement):
    mov = movement.replace("u", "↑").replace("r", "→").replace("d", "↓").replace("l", "←")

    solution[point[0]][point[1]] = mov

    for i in range(0, len(solution)):
        line = ''
        for j in range(0, len(solution[i])):
            line += solution[i][j]
        print(line)
    print('\n')

    return solution


def print_map(summits):
    for line in range(0, len(summits)):
        print_line = ''
        for column in range(0, len(summits[line])):
            element = str(summits[line][column])

            if len(element) == 1:
                if element.isnumeric():
                    element = '0' + element
                else:
                    element += element

            print_line += element + " "
        print(f"{print_line}")


def main():
    start_sign = 'S'
    end_sign = 'E'

    summits = []

    for line in open('inp.txt', 'r'):
        line = list(line.strip())

        heights = []
        for element in line:
            if element == start_sign or element == end_sign:
                heights.append(element)
            else:
                heights.append(str(alphabet.index(element)))

        summits.append(heights)

    # Visual map to help debugging
    print_map(summits)

    start = ()
    end = ()
    for line in range(0, len(summits)):
        for column in range(0, len(summits[line])):
            element = str(summits[line][column])
            if element == start_sign:
                start = (line, column)
            elif element == end_sign:
                end = (line, column)

    solution_map = [['.' for _ in range(0, len(summits[x]))] for x in range(len(summits))]
    solution_map[start[0]][start[1]] = 'S'
    solution_map[end[0]][end[1]] = 'E'

    visited = set()
    bfs(summits, visited, start, end)


if __name__ == "__main__":
    main()
