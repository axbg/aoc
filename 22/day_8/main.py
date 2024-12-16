def format_tree(i, j):
    return f"{i},{j}"


def current_tree_visible(current_tree, previous_tree):
    return current_tree > previous_tree


def main():
    trees = []
    for line in open('inp.txt', 'r'):
        trees.append(list(line.strip()))

    visible_trees = set()

    size = len(trees)

    for i in range(0, size):
        for j in range(0, size):
            if i == 0 or i == (size - 1) or j == 0 or j == (size - 1):
                visible_trees.add(format_tree(i, j))

    # count from top
    for j in range(1, size - 1):
        biggest = trees[0][j]
        for i in range(1, size - 1):
            if current_tree_visible(trees[i][j], biggest):
                visible_trees.add(format_tree(i, j))
                biggest = trees[i][j]

    # count from bottom
    for j in range(1, size - 1):
        biggest = trees[size - 1][j]
        for i in range(size - 2, 0, -1):
            if current_tree_visible(trees[i][j], biggest):
                visible_trees.add(format_tree(i, j))
                biggest = trees[i][j]

    # count from left
    for i in range(1, size - 1):
        biggest = trees[i][0]
        for j in range(1, size - 1):
            if current_tree_visible(trees[i][j], biggest):
                visible_trees.add(format_tree(i, j))
                biggest = trees[i][j]

    # count from right
    for i in range(1, size - 1):
        biggest = trees[i][size - 1]
        for j in range(size - 1, 0, -1):
            if current_tree_visible(trees[i][j], biggest):
                visible_trees.add(format_tree(i, j))
                biggest = trees[i][j]

    print(f"There are {len(visible_trees)} visible trees")


if __name__ == "__main__":
    main()
