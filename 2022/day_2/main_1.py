score = 0

ROCK = "A"
PAPER = "B"
SCISSOR = "C"


def convert(type):
    if "X" == type:
        return ROCK
    elif "Z" == type:
        return SCISSOR
    else:
        return PAPER


def print_type(type):
    if ROCK == type:
        return "ROCK"
    elif SCISSOR == type:
        return "SCISSOR"
    else:
        return "PAPER"


with open("inp.txt", "r") as file:
    rnd_chs = 0
    rnd_res = 0

    for line in file:
        [op, me] = line.strip().split(" ")
        me = convert(me)

        if ROCK == me:
            rnd_chs = 1
        elif PAPER == me:
            rnd_chs = 2
        else:
            rnd_chs = 3

        if op == me:
            rnd_res = 3
        elif (op == ROCK and me == SCISSOR) or (op == SCISSOR and me == PAPER) or (op == PAPER and me == ROCK):
            rnd_res = 0
        else:
            rnd_res = 6

        score += rnd_chs
        score += rnd_res
        print(f"Opponent chose {print_type(op)}, I chose {print_type(me)}: the score is: {rnd_chs} + {rnd_res}")

print(f"the score is {score}")
