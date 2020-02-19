# Given a directed graph, find the route between two nodes

# Idea: BFS

graph = {
    'a': ['b', 'd'],
    'b': ['e'],
    'c': ['e', 'f'],
    'd': ['b'],
    'e': ['g', 'd'],
    'f': [],
    'g': ['c']
}

# Find route between A and V

from queue import Queue

def bfs(start_node, end_node, graph):
    # Do a BFS search from start node

    parents = { start_node: None }

    queue = Queue()

    queue.put(start_node)

    while not queue.empty():
        # Get neighbor nodes

        current_node = queue.get()

        neighbors = graph[current_node]

        if len(neighbors) == 0:
            continue

        found_end_node = False

        for neighbor in neighbors:
            if neighbor in parents:
                continue

            parents[neighbor] = current_node

            if neighbor == end_node:
                found_end_node = True

                break

            queue.put(neighbor)

        if found_end_node:
            break

    return parents


def find_route(start_node, end_node, graph):
    parents = bfs(start_node, end_node, graph)

    if end_node not in parents:
        return None

    route = []

    route.append(end_node)

    current_node = parents[end_node]

    # Iterate until we reach the parent node
    while True:
        route.append(current_node)

        if current_node == start_node:
            # We're done, we found what we were looking for
            break

        current_node = parents[current_node]

    route.reverse()

    return route


print(find_route('a', 'g', graph))
