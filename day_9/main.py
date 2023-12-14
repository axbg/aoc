from math import dist, floor


def compute_position(tail):
    return f"{tail[0]},{tail[1]}"


def move_head(head, direction):
    if direction == "L":
        new_head = (head[0] - 1, head[1])
    elif direction == "R":
        new_head = (head[0] + 1, head[1])
    elif direction == "U":
        new_head = (head[0], head[1] + 1)
    else:
        # D
        new_head = (head[0], head[1] - 1)

    return new_head


def compute_distance(head, tail):
    return dist([head[0], head[1]], [tail[0], tail[1]])


# This method
# Look into main_2.py to see its proper implementation
# (I left it here just as a reminder of my initial approach of solving this challenge)
def move_tail(head, tail, direction):
    distance = floor(compute_distance(head, tail))
    xh = head[0]
    yh = head[1]
    xt = tail[0]
    yt = tail[1]

    if distance > 1:
        if direction == 'L':
            if yh == yt:
                xt -= 1
            else:
                yt = yh
                xt = xh + 1

        elif direction == 'R':
            if yh == yt:
                xt += 1
            else:
                yt = yh
                xt = xh - 1

        elif direction == 'U':
            if xh == xt:
                yt += 1
            else:
                xt = xh
                yt = yh - 1

        else:
            if xh == xt:
                yt -= 1
            else:
                xt = xh
                yt = yh + 1

        return xt, yt
    else:
        return tail


def main():
    positions = set()

    head = (0, 0)
    tail = (0, 0)
    positions.add(compute_position(tail))

    for line in open('inp.txt', 'r'):
        [direction, steps] = line.strip().split(" ")

        for i in range(0, int(steps)):
            head = move_head(head, direction)
            tail = move_tail(head, tail, direction)
            positions.add(compute_position(tail))

    print(f"The tail has been in {len(positions)} positions")


if __name__ == "__main__":
    main()
