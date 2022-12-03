ROCK = "A"
PAPER = "B"
SCISSOR = "C"

LOSE = "X"
WIN = "Z"
DRAW = "Y"


def print_type(typ):
    if ROCK == typ:
        return "ROCK"
    elif SCISSOR == typ:
        return "SCISSOR"
    else:
        return "PAPER"


def main():
    score = 0

    with open("inp.txt", "r") as file:
        for line in file:
            [op, result] = line.strip().split(" ")

            me = ""

            if result == DRAW:
                me = op
            elif result == WIN:
                if op == SCISSOR:
                    me = ROCK
                elif op == ROCK:
                    me = PAPER
                elif op == PAPER:
                    me = SCISSOR
            elif result == LOSE:
                if op == SCISSOR:
                    me = PAPER
                elif op == ROCK:
                    me = SCISSOR
                elif op == PAPER:
                    me = ROCK

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

            score += (rnd_chs + rnd_res)
            print(f"Opponent chose {print_type(op)}, I chose {print_type(me)}: the score is: {rnd_chs} + {rnd_res}")

    print(f"the score is {score}")


if __name__ == "__main__":
    main()
