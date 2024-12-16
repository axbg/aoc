from more_itertools import set_partitions

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


def get_combinations(arr):
    return list(set_partitions(arr, 2))


def main():
    movements = 26
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

    biggest = 0
    s1 = []
    s2 = []
    results = []

    # Generate all the possible combinations of splitting the list in 2 separate sets
    combinations = get_combinations(list(map(lambda x: x[1].name, positive_nodes.items())))

    # Will iterate through each pair and will compute the scores independently
    # The biggest score will be the optimal solution
    for combination in combinations:
        d1 = {}
        for element in combination[0]:
            d1[element] = positive_nodes[element]

        d2 = {}
        for element in combination[1]:
            d2[element] = positive_nodes[element]

        result = compute_result(d1, {}, nodes['AA'], movements) + compute_result(d2, {}, nodes['AA'], movements)
        results.append({'result': result, 's1': combination[0], 's2': combination[1]})

        if result > biggest:
            biggest = result
            s1 = combination[0]
            s2 = combination[1]

    # Save all the results in a file for debug purposes
    results.sort(key=lambda x: x['result'], reverse=True)
    with open('result', 'w+') as resfile:
        for result in results:
            resfile.write(f"{result['result']}: {result['s1']} - {result['s2']}\n")

    print(f"The result is {biggest} for lists {s1} and {s2}")


if __name__ == "__main__":
    main()
