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


# For the second challenge I realized that the way I've written this method is wrong,
# so I've rewritten it from scratch, using only the position of the head to determine
# how the tail should move

# This method works for the first challenge too
def move_tail(head, tail):
    distance = floor(compute_distance(head, tail))
    xh = head[0]
    yh = head[1]
    xt = tail[0]
    yt = tail[1]

    if distance > 1:
        if xh == xt:
            if yh > yt:
                yt += 1
            else:
                yt -= 1
        elif yh == yt:
            if xh > xt:
                xt += 1
            else:
                xt -= 1
        else:
            if xh < xt:
                xt -= 1
            else:
                xt += 1

            if yh < yt:
                yt -= 1
            else:
                yt += 1

        return xt, yt
    else:
        return tail


def main():
    positions = set()

    head = (0, 0)
    tails = [(0, 0) for _ in range(0, 9)]
    positions.add(compute_position((0, 0)))

    for line in open('inp.txt', 'r'):
        [direction, steps] = line.strip().split(" ")

        for i in range(0, int(steps)):
            head = move_head(head, direction)
            tails[0] = move_tail(head, tails[0])

            for j in range(1, 9):
                tails[j] = move_tail(tails[j - 1], tails[j])

            positions.add(compute_position(tails[8]))

    print(f"The tail has been in {len(positions)} positions")


if __name__ == "__main__":
    main()
