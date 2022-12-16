import threading


def get_point(info_line):
    sensor_info = info_line.split(', ')
    x = int(sensor_info[0].split('=')[1])
    y = int(sensor_info[1].split('=')[1])

    return {'x': y, 'y': x}


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def compute_result(x, y):
    return y * 4000000 + x


def check_limits(sensor, beacon, min, max, sensors, beacons):
    result = []
    perimeter_limit = manhattan_distance(sensor['x'], sensor['y'], beacon['x'], beacon['y'])

    # top left
    x = sensor['x'] - perimeter_limit - 1
    y = sensor['y']
    while x <= sensor['x']:
        found = True

        if min <= x <= max and min <= y <= max:
            for sensor2, beacon2 in zip(sensors, beacons):
                if manhattan_distance(sensor2['x'], sensor2['y'], beacon2['x'], beacon2['y']) >= manhattan_distance(
                        sensor2['x'], sensor2['y'], x, y):
                    found = False
                    break
        else:
            found = False

        if found:
            print(f"The point is: {x},{y}. The result is {compute_result(x, y)}")
            exit(0)

        x += 1
        y -= 1

    # top right
    x = sensor['x']
    y = sensor['y'] - perimeter_limit - 1
    while y <= sensor['y']:
        found = True

        if min <= x <= max and min <= y <= max:
            for sensor2, beacon2 in zip(sensors, beacons):
                if manhattan_distance(sensor2['x'], sensor2['y'], beacon['x'], beacon['y']) >= manhattan_distance(
                        sensor2['x'], sensor2['y'], x, y):
                    found = False
                    break
        else:
            found = False

        if found:
            print(f"The point is: {x},{y}. The result is {compute_result(x, y)}")
            exit(0)

        x -= 1
        y += 1

    # bottom right
    x = sensor['x'] - perimeter_limit + 1
    y = sensor['y']
    while x >= sensor['x']:
        found = True

        if min <= x <= max and min <= y <= max:
            for sensor2, beacon2 in zip(sensors, beacons):
                if manhattan_distance(sensor2['x'], sensor2['y'], beacon['x'], beacon['y']) >= manhattan_distance(
                        sensor2['x'], sensor2['y'], x, y):
                    found = False
                    break
        else:
            found = False

        if found:
            print(f"The point is: {x},{y}. The result is {compute_result(x, y)}")
            exit(0)

        x -= 1
        y += 1

    # bottom left
    x = sensor['x']
    y = sensor['y'] - perimeter_limit + 1
    while y >= sensor['y']:
        found = True

        if min <= x <= max and min <= y <= max:
            for sensor2, beacon2 in zip(sensors, beacons):
                if manhattan_distance(sensor2['x'], sensor2['y'], beacon['x'], beacon['y']) >= manhattan_distance(
                        sensor2['x'], sensor2['y'], x, y):
                    found = False
                    break
        else:
            found = False

        if found:
            print(f"The point is: {x},{y}. The result is {compute_result(x, y)}")
            exit(0)

        x -= 1
        y -= 1

    return result


def main():
    sensors = []
    beacons = []
    for line in open('inp.txt', 'r'):
        line = line.strip().split(":")
        sensors.append(get_point(line[0]))
        beacons.append(get_point(line[1]))

    min = 0
    max = 4000000

    for sensor, beacon in zip(sensors, beacons):
        check_limits(sensor, beacon, min, max, sensors, beacons)


if __name__ == "__main__":
    main()
