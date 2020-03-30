from practice.node_prio_queue import *

g = {
    'G': [('Y', 19), ('P', 7)],
    'Y': [('R', 4), ('P', 11), ('G', 19)],
    'P': [('G', 7), ('Y', 11), ('B', 5), ('R', 15)],
    'R': [('Y', 4), ('P', 15), ('B', 13)],
    'B': [('P', 5), ('R', 13)]
}

start = 'G'
end = 'B'

distances = NodesPrioQueue()

current_node = start

visited_nodes = {start: 1}
path = []

path.append(start)

while True:
    # Relax edges from current node
    edges = g[current_node]

    distances.purge()

    for edge in edges:
        if edge[0] in visited_nodes:
            continue

        distances.insert(Node(edge[0], edge[1]))

    # Get shortest distance
    shortest = distances.getLowest()

    if shortest is None:
        print("Woops, seems like we cant go nowhere from node {}".format(current_node))

        break

    print("Moving from {} to {}".format(current_node, shortest.label))

    current_node = shortest.label

    visited_nodes[current_node] = 1

    path.append(current_node)

    if current_node == end:
        print("We reached the end node: {}! Stopping algo.".format(current_node))

        break


print("Path is: {}".format(" -> ".join(path)))