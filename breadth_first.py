# So one option to represent the graphs is using adjacency list. Adjacency list is an array where each element corresponds
# to one vertex and has a pointer to it's neighbor nodes. We can either use array or dictionary. If using array, nodes
# are indexed 0 to n - 1, and if using dictionary, we can index by the key itself

from queue import Queue

adj_list = [
    # 0 --> a
    [2],       # A points to [c] only
    # 1 --> b
    [0, 2],    # B points to [a, c]
    # 2 --> c  # C points to [b]
    [1]
]

# Another way is to use linked classes I guess

class Vertex:
    def __init__(self, key, neighbors):
        self.__key = key
        self.__neighbors = neighbors

    def get_key(self):
        return self.__key

    def get_neighbors(self):
        return self.__neighbors

# vertices = [
#     Vertex('a', ['c']),
#     Vertex('b', ['a', 'b']),
#     Vertex('c', ['b'])
# ]


# Example -- find path from "s" to "v"
# Let's use the dictionaries for storing what can go where

vertices = {
    'a': ['b', 'c', 's'],
    'b': ['a'],
    'c': ['a', 's'],
    'd': ['s', 'e', 'f'],
    'e': ['s', 'd', 'f', 'v'],
    'f': ['d', 'e', 'f'],
    's': ['a', 'c', 'd', 'e'],
    'v': ['e', 'f']
}

def get_neighbors(vertex):
    """Returns neighbors of a given vertex"""
    return vertices[vertex]

def bfs(start_vertex):
    """Breadth-first search -- starting from given vertex"""

    # Hashmap of visited notes
    visited = {start_vertex: True}

    parent = {start_vertex: None}

    # Nodes that we are going to iterate
    frontier = Queue()

    frontier.put(start_vertex)

    while not frontier.empty():
        vertex = frontier.get()

        print("Visiting node: {}".format(vertex))

        for neighbor in get_neighbors(vertex):
            if neighbor not in visited:
                visited[neighbor] = True

                parent[neighbor] = vertex

                frontier.put(neighbor)

    return parent


parents = bfs('s')

# So now let's see how to get from 'v' to 's'

current_node = 'v'

destination_node = 's'

path = []

while True:
    path.append(current_node)

    if parents[current_node] is None:
        break

    current_node = parents[current_node]

    if current_node == destination_node:
        print("Destination reached!")
        break
print(path)





