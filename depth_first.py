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

    visiting[start_node] = True

    for neighbor in neighbors:

        if neighbor in visiting:
            print("Found a back-edge from {} to {}".format(start_node, neighbor))

        if neighbor not in parents:
            parents[neighbor] = start_node

            depth_first_search(neighbor, adjacency_list, parents, visiting)

    del visiting[start_node]

    visiting_order.append(start_node)

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

print("New graph!!!")

graph = {
    5: [11],
    7: [8, 11],
    3: [8, 10],
    11: [2, 9, 10],
    8: [9],
    2: [],
    9: [],
    10: []
}

visiting_order = []

parents = {}

for vertex in graph.keys():
    if vertex in parents:
        continue

    parents[vertex] = None

    depth_first_search(vertex, graph, parents, visiting = {})

visiting_order.reverse()
print(visiting_order)