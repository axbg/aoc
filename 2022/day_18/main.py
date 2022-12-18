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

    mapp = [[['0' for _ in range(0, highest_z)] for _ in range(0, highest_y)] for _ in range(0, highest_x)]

    for line in lines:
        line = line.strip()
        [x, y, z] = line.strip().split(',')
        x = int(x)
        y = int(y)
        z = int(z)

        mapp[x][y][z] = 1

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


if __name__ == "__main__":
    main()
