def format_tree(i, j):
    return f"{i},{j}"


def current_tree_visible(current_tree, previous_tree):
    return current_tree > previous_tree


def main():
    trees = []
    for line in open('inp.txt', 'r'):
        trees.append(list(line.strip()))

    size = len(trees)
    max_score = 0

    for i in range(1, size - 1):
        for j in range(1, size - 1):
            top_score = 0
            bottom_score = 0
            left_score = 0
            right_score = 0

            # compute top
            for ii in range(i - 1, -1, -1):
                top_score += 1
                if trees[i][j] <= trees[ii][j]:
                    break

            # compute bottom
            for ii in range(i + 1, size):
                bottom_score += 1
                if trees[i][j] <= trees[ii][j]:
                    break

            # compute left
            for jj in range(j - 1, -1, -1):
                left_score += 1
                if trees[i][j] <= trees[i][jj]:
                    break

            # compute right
            for jj in range(j + 1, size):
                right_score += 1
                if trees[i][j] <= trees[i][jj]:
                    break

            local_score = top_score * bottom_score * left_score * right_score

            if local_score > max_score:
                max_score = local_score

    print(f"The maximum scenic score is {max_score}")


if __name__ == "__main__":
    main()
