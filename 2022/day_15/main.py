def get_point(info_line):
    sensor_info = info_line.split(', ')
    x = int(sensor_info[0].split('=')[1])
    y = int(sensor_info[1].split('=')[1])

    return {'x': y, 'y': x}


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def compute_direction(x, y, increment_y, distance, line_to_check, min_y, max_y):
    new_x = line_to_check
    new_y = y

    results = []
    while manhattan_distance(x, y, line_to_check, new_y) <= distance and min_y <= new_y <= max_y:
        results.append((new_x, new_y))
        new_y += increment_y

    return results


def main():
    search_line = 10

    sensors = []
    beacons = []
    for line in open('inp.txt', 'r'):
        line = line.strip().split(":")
        sensors.append(get_point(line[0]))
        beacons.append(get_point(line[1]))

    max_y = sensors[0]['y']
    min_y = sensors[0]['y']

    for sensor, beacon in zip(sensors, beacons):
        if sensor['y'] > max_y:
            max_y = sensor['y']
        elif sensor['y'] < min_y:
            min_y = sensor['y']

        if beacon['y'] > max_y:
            max_y = beacon['y']
        elif beacon['y'] < min_y:
            min_y = beacon['y']

    not_beacon = set()
    for sensor, beacon in zip(sensors, beacons):
        closest_distance = manhattan_distance(sensor['x'], sensor['y'], beacon['x'], beacon['y'])

        r2 = compute_direction(sensor['x'], sensor['y'], 1, closest_distance, search_line, min_y, max_y)
        r1 = compute_direction(sensor['x'], sensor['y'], -1, closest_distance, search_line, min_y, max_y)

        not_beacon.update(r1)
        not_beacon.update(r2)

    not_beacon = list(not_beacon)
    legit_no_beacons = set()
    for spot in not_beacon:
        for beacon in beacons:
            if spot[0] == beacon['x'] and spot[1] != beacon['y']:
                legit_no_beacons.add(spot)

    not_beacon = list(legit_no_beacons)
    not_beacon.sort(key=lambda x: x[1])

    print(len(not_beacon))


if __name__ == "__main__":
    main()
