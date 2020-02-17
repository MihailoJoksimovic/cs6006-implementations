# Implement depth first graph search. Try implementing edge classification and topological sort as well

# How to represent graphs? 1. Adjacency lists, 2. Objects

graph = {
    'a': ['b', 'd'],
    'b': ['e'],
    'c': ['e', 'f'],
    'd': ['b'],
    'e': ['d', 'g'],
    'f': [],
    'g': ['d']
}

visiting_order = []


def depth_first_search(start_node, adjacency_list, parents, visiting):
    neighbors = adjacency_list[start_node]

    print("Visiting {}".format(start_node))

    visiting_order.append(start_node)

    if len(neighbors) == 0:
        # This is a leaf node :)
        return

    visiting[start_node] = True

    for neighbor in neighbors:

        if neighbor in visiting:
            print("Found a back-edge from {} to {}".format(start_node, neighbor))

        if neighbor not in parents:
            parents[neighbor] = start_node

            depth_first_search(neighbor, adjacency_list, parents, visiting)

    del visiting[start_node]

# depth_first_search('a', graph)

# Now lets make sure to visit ALL vertices

parents = {}

for vertex in graph.keys():
    if vertex in parents:
        continue

    parents[vertex] = None

    depth_first_search(vertex, graph, parents, visiting = {})

visiting_order.reverse()
print(visiting_order)

