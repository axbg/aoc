def check_visited(coord1, visited_list):
    for coord2 in visited_list:
        if coord1[0] == coord2[0] and coord1[1] == coord2[1] and coord1[2] == coord2[2]:
            return True

    return False


def main():
    lines = open('inp.txt', 'r').readlines()

    highest_x = 0
    highest_y = 0
    highest_z = 0
    for line in lines:
        [x, y, z] = line.strip().split(',')
        x = int(x)
        y = int(y)
        z = int(z)

        if x > highest_x:
            highest_x = x
        if y > highest_y:
            highest_y = y
        if z > highest_z:
            highest_z = z

    highest_x += 1
    highest_y += 1
    highest_z += 1

    mapp = [[[0 for _ in range(0, highest_z)] for _ in range(0, highest_y)] for _ in range(0, highest_x)]

    for line in lines:
        line = line.strip()
        [x, y, z] = line.strip().split(',')
        x = int(x)
        y = int(y)
        z = int(z)

        mapp[x][y][z] = 1

    # compute sum from step 1
    total_sides = 0
    for x in range(0, highest_x):
        for y in range(0, highest_y):
            for z in range(0, highest_z):
                if mapp[x][y][z] == 1:
                    sides = 6

                    try:
                        if z - 1 >= 0:
                            if mapp[x][y][z - 1] == 1:
                                sides -= 1
                    except:
                        pass

                    try:
                        if mapp[x][y][z + 1] == 1:
                            sides -= 1
                    except:
                        pass

                    try:
                        if y - 1 >= 0:
                            if mapp[x][y - 1][z] == 1:
                                sides -= 1
                    except:
                        pass

                    try:
                        if mapp[x][y + 1][z] == 1:
                            sides -= 1
                    except:
                        pass

                    try:
                        if x - 1 >= 0:
                            if mapp[x - 1][y][z] == 1:
                                sides -= 1
                    except:
                        pass

                    try:
                        if mapp[x + 1][y][z] == 1:
                            sides -= 1
                    except:
                        pass

                    total_sides += sides

    print(f'Total visible sides: {total_sides}')

    # compute trapped air
    air = [(0, 0, 0)]
    visited_air = []
    while len(air) > 0:
        current = air.pop()
        visited_air.append(current)

        try:
            if current[2] - 1 >= 0:
                if not check_visited((current[0], current[1], current[2] - 1), visited_air) \
                        and mapp[current[0]][current[1]][current[2] - 1] == 0:
                    air.append((current[0], current[1], current[2] - 1))
        except:
            pass

        try:
            if not check_visited((current[0], current[1], current[2] + 1), visited_air) \
                    and mapp[current[0]][current[1]][current[2] + 1] == 0:
                air.append((current[0], current[1], current[2] + 1))
        except:
            pass

        try:
            if current[1] - 1 >= 0:
                if not check_visited((current[0], current[1] - 1, current[2]), visited_air) \
                        and mapp[current[0]][current[1] - 1][current[2]] == 0:
                    air.append((current[0], current[1] - 1, current[2]))
        except:
            pass

        try:
            if not check_visited((current[0], current[1] + 1, current[2]), visited_air) and \
                    mapp[current[0]][current[1] + 1][current[2]] == 0:
                air.append((current[0], current[1] + 1, current[2]))
        except:
            pass

        try:
            if current[0] - 1 >= 0:
                if not check_visited((current[0] - 1, current[1], current[2]), visited_air) and \
                        mapp[current[0] - 1][current[1]][current[2]] == 0:
                    air.append((current[0] - 1, current[1], current[2]))
        except:
            pass

        try:
            if not check_visited((current[0] + 1, current[1], current[2]), visited_air) and \
                    mapp[current[0] + 1][current[1]][current[2]] == 0:
                air.append((current[0] + 1, current[1], current[2]))
        except:
            pass

    trapped_air = []
    for x in range(0, highest_x):
        for y in range(0, highest_y):
            for z in range(0, highest_z):
                if mapp[x][y][z] == 0 and (x, y, z) not in visited_air:
                    trapped_air.append((x, y, z))

    print(f"The following air is trapped {trapped_air}")

    for air in trapped_air:
        x = air[0]
        y = air[1]
        z = air[2]

        try:
            if z - 1 >= 0:
                if mapp[x][y][z - 1] == 1:
                    total_sides -= 1
        except:
            pass

        try:
            if mapp[x][y][z + 1] == 1:
                total_sides -= 1
        except:
            pass

        try:
            if y - 1 >= 0:
                if mapp[x][y - 1][z] == 1:
                    total_sides -= 1
        except:
            pass

        try:
            if mapp[x][y + 1][z] == 1:
                total_sides -= 1
        except:
            pass

        try:
            if x - 1 >= 0:
                if mapp[x - 1][y][z] == 1:
                    total_sides -= 1
        except:
            pass

        try:
            if mapp[x + 1][y][z] == 1:
                total_sides -= 1
        except:
            pass

    print(f"New visible total sides: {total_sides}")

if __name__ == "__main__":
    main()
