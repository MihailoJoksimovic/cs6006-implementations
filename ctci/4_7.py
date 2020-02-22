# Build order --> given a list of projects, sort them in an order so that the projects that dont depend on anything else
# are solved first.

edges = {
    'a': ['d'],
    'b': ['d'],
    'c': ['a'], # This one makes is cyclic! Remove when testing DAG ;)
    'd': ['c'],
    'e': [],
    'f': ['a', 'b']
}

visit_order = []

# Idea: traverse the graph by depth and make sure there are no backlinks

def dfs(vertex, edges, parents, visiting, visit_order):
    print("Entering {}".format(vertex))

    visiting[vertex] = True

    neighbors = edges[vertex]

    print("Neighbors: {}".format(neighbors))

    for neighbor in neighbors:
        if neighbor in visiting:
            print("\tWuopa, found a back-edge from {} to {}!".format(vertex, neighbor))

        if neighbor in parents:
            print("\tNeighbor {} already visited. Skipping".format(neighbor))

            raise Exception("Graph is not acyclic!")

        parents[neighbor] = vertex

        print("\tVisiting neighbor: {}".format(neighbor))

        dfs(neighbor, edges, parents, visiting, visit_order)

    print("Visiting node {}".format(vertex))

    del visiting[vertex]

    visit_order.append(vertex)

parents = {}
visiting = {}

for vertex in edges.keys():
    if vertex in parents:
        continue

    parents[vertex] = None

    dfs(vertex, edges, parents, visiting, visit_order)

visit_order.reverse()

print(visit_order)