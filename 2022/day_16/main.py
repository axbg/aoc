from copy import deepcopy


class Node:
    def __init__(self, name, value, links):
        self.name = name
        self.value = int(value)
        self.links = links
        self.distances = {}

    def add_distance(self, node, distance):
        if node not in self.distances:
            self.distances[node] = distance


# Start a given node and compute all the possible paths downwards in the remaining amount of time
# From all these paths, choose the best one and add it up to the value of the current node
def compute_result(nodes, visited, start_node, time):
    if start_node.value > 0:
        time -= 1

    score = time * start_node.value
    visited[start_node.name] = 1

    biggest_link_score = 0
    for link in nodes:
        if link not in visited and (time - start_node.distances[link] - 1) >= 0:
            link_result = compute_result(nodes, deepcopy(visited), nodes[link], time - start_node.distances[link])

            if link_result > biggest_link_score:
                biggest_link_score = link_result

    return score + biggest_link_score


def main():
    movements = 30
    nodes = {}

    for line in open('inp.txt', 'r'):
        line = line.strip().replace("valve ", "valves ").split(";")

        name = line[0].split(' ')[1]
        value = line[0].split('=')[1]
        neighbours = line[1].split('valves ')[1].split(', ')

        nodes[name] = (Node(name, value, neighbours))

    for node in dict.keys(nodes):
        visited = set()
        current = set()

        current.add(nodes[node].name + '#0')

        while len(visited) != len(nodes) and len(current) != 0:
            current_info = current.pop()
            [name, distance] = current_info.split("#")
            current_node = nodes[name]

            visited.add(current_node.name)

            distance = int(distance) + 1

            for node_name in current_node.links:
                if node_name not in visited:
                    current.add(node_name + '#' + str(distance))
                    nodes[node].add_distance(node_name, distance)

    positive_nodes = dict(filter(lambda x: x[1].value > 0, nodes.items()))
    result = compute_result(positive_nodes, {}, nodes['AA'], movements)
    print(result)


if __name__ == "__main__":
    main()
