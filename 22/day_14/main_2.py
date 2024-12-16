def extract_points(point):
    coords = point.split(",")
    return (int(coords[1]), int(coords[0]))


def draw_path(map, start, end):
    start_point = extract_points(start)
    end_point = extract_points(end)

    while start_point[0] != end_point[0] or start_point[1] != end_point[1]:
        map[start_point[0]][start_point[1]] = '#'

        if start_point[0] < end_point[0]:
            start_point = (start_point[0] + 1, start_point[1])
        elif start_point[0] > end_point[0]:
            start_point = (start_point[0] - 1, start_point[1])

        if start_point[1] < end_point[1]:
            start_point = (start_point[0], start_point[1] + 1)
        elif start_point[1] > end_point[1]:
            start_point = (start_point[0], start_point[1] - 1)

    map[end_point[0]][end_point[1]] = '#'

    return map


def print_map(map):
    for i in range(0, len(map)):
        line = ''
        for j in range(0, len(map[i])):
            line += map[i][j]
        print(f"{line}")


def init_map(lines):
    start_point = (0, 500)
    end_point = (0, 500)
    origin_point = (0, 500)

    for line in lines:
        paths = line.strip().split(" -> ")

        for element in paths:
            [y, x] = element.split(",")
            x = int(x)
            y = int(y)

            if y < start_point[1]:
                start_point = (start_point[0], y)

            if y > end_point[1]:
                end_point = (end_point[0], y)

            if x > end_point[0]:
                end_point = (x, end_point[1])

    end_point = (end_point[0] + 3, end_point[1] * 2 + 1)

    map = []
    for i in range(0, end_point[0]):
        content = []
        for j in range(0, end_point[1]):
            content.append(".")
        map.append(content)

    map[origin_point[0]][origin_point[1]] = '+'

    for i in range(end_point[0] - 1, end_point[0]):
        for j in range(0, end_point[1]):
            map[i][j] = '#'

    return [map, origin_point]


def drop_sand(map, origin):
    is_ok = True

    x = origin[0]
    y = origin[1]

    while is_ok:
        if map[x + 1][y] == '.':
            x += 1
        elif map[x + 1][y - 1] == '.':
            x += 1
            y -= 1
        elif map[x + 1][y + 1] == '.':
            x += 1
            y += 1
        else:
            is_ok = False

    return (x, y)


def arrange_sand(map, origin):
    while 1:
        position = drop_sand(map, origin)

        if position[0] == origin[0] and position[1] == origin[1]:
            break

        map[position[0]][position[1]] = 'o'

    return map


def main():
    with open('inp.txt', 'r') as file:
        lines = file.readlines()

    [map, origin] = init_map(lines)

    for line in lines:
        points = line.strip().split(" -> ")

        for i in range(0, len(points) - 1):
            map = draw_path(map, points[i], points[i + 1])

    # for debug purposes
    # print_map(map)

    map = arrange_sand(map, origin)
    print_map(map)

    ct = 1
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 'o':
                ct += 1

    print(f"Solution is {ct}")


if __name__ == "__main__":
    main()
