class Node:
    def __init__(self, name, is_dir, size, parent):
        self.name = name
        self.children = []
        self.size = size
        self.is_dir = is_dir
        self.parent = parent

    def add_children(self, child):
        self.children.append(child)

    def get_children(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def get_parent(self):
        return self.parent

    def get_tree(self, level):
        display_level = "".join(['-' for x in range(0, level)])

        if self.is_dir:
            tag = f"{display_level}{self.name} dir\n"
        else:
            tag = f"{display_level}{self.name} {self.size}\n"

        for child in self.children:
            tag += child.get_tree(level + 1)

        return tag

    def get_size(self):
        if not self.is_dir:
            return self.size

        size = 0
        for child in self.children:
            size += child.get_size()

        return size

    def get_size_sum_with_threshold(self, threshold):
        if not self.is_dir:
            return 0

        size = self.get_size()
        total_sum = 0
        if size < threshold:
            total_sum += size

        for child in self.children:
            total_sum += child.get_size_sum_with_threshold(threshold)

        return total_sum

    def __str__(self):
        return self.name


def main():
    command = '$'
    cd = 'cd'
    back = '..'
    dir = 'dir'

    root = Node('root', True, 0, None)

    current_node = root
    for line in open('inp.txt', 'r'):
        exploded = line.strip().split(" ")
        if exploded[0] == command:
            if exploded[1] == cd:
                if exploded[2] == back:
                    current_node = current_node.get_parent()
                else:
                    current_node = current_node.get_children(exploded[2])
        if exploded[0] == dir:
            current_node.add_children(Node(exploded[1], True, 0, current_node))
        elif exploded[0].isnumeric():
            current_node.add_children(Node(exploded[1], False, int(exploded[0]), current_node))

    # display the tree
    # print(root.get_tree(0))

    # display the size of a file or dir
    # print(root.get_size())

    # display the sum of all directories under a certain threshold
    print(root.get_size_sum_with_threshold(100000))


if __name__ == "__main__":
    main()
