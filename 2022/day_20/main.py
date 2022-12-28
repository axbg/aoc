class Node:
    def __init__(self, position, value, prev):
        self.position = position
        self.value = value
        self.prev = prev
        self.next = None


def debug_list(first):
    result = [str(first.value)]

    node = first.next
    while node.position != first.position:
        result.append(str(node.value))
        node = node.next

    print(f"{', '.join(result)}\n")


def skip_elements(zero_element, length, to_skip):
    to_parse = to_skip % length

    next = zero_element
    for i in range(0, to_parse):
        next = next.next

    return next.value


def main():
    read_first = False

    counter = 1
    prev = None
    first = None
    for line in open("inp.txt", "r"):
        node = Node(counter, int(line.strip()), prev)
        counter += 1

        if prev is not None:
            prev.next = node

        prev = node

        if read_first is False:
            first = node
            read_first = True

    first.prev = node
    node.next = first

    # debug_list(first)
    for i in range(1, counter):
        node = first

        while True:
            if node.position == i:
                break
            node = node.next

        if node.value != 0:
            # Link previous neighbours in order to remove the current node from list
            node.prev.next = node.next
            node.next.prev = node.prev

            # The list has one less element now
            to_skip = node.value % (counter - 2)

            new_prev = node.prev
            for _ in range(to_skip):
                new_prev = new_prev.next

            node.prev = new_prev
            node.next = new_prev.next
            node.prev.next = node
            node.next.prev = node

            # debug_list(first)

    # Find 0
    zero_node = first
    while True:
        if zero_node.value == 0:
            break
        zero_node = zero_node.next

    c1 = skip_elements(zero_node, counter - 1, 1000)
    c2 = skip_elements(zero_node, counter - 1, 2000)
    c3 = skip_elements(zero_node, counter - 1, 3000)

    print(c1 + c2 + c3)


if __name__ == "__main__":
    main()
