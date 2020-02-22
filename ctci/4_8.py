# Design an algo. to find a first common ancestor of two nodes in a binary tree (NOTE: this tree IS NOT a binary search tree!)
# Avoid storing additional nodes in a Data Structure

from ctci.common.classes import *

class DiscoverableNode(Node):
    def __init__(self, key, left_child = None, right_child = None, parent = None):
        super().__init__(key, left_child, right_child, parent)

        self.discovered = False

    def neighbors(self):
        neighbors = []

        if self.left_child:
            neighbors.append(self.left_child)

        if self.right_child:
            neighbors.append(self.right_child)

        return neighbors

g = DiscoverableNode('g')
f = DiscoverableNode('f', g)
e = DiscoverableNode('e', f)
d = DiscoverableNode('d')
b = DiscoverableNode('b', d, e)
k = DiscoverableNode('k')
j = DiscoverableNode('j')
i = DiscoverableNode('i', j, k)
h = DiscoverableNode('h', None, i)
c = DiscoverableNode('c', None, h)
a = DiscoverableNode('a', b, c)


# Idea: First find path to both. Then implement method to find a FIRST descendant of both nodes. We would do BFS here.
# I think that its absolutely the same whether we use DFS or BFS here

# Runtime: O(n)
def discover_path_to_nodes(root_node: DiscoverableNode, first_node: DiscoverableNode, second_node: DiscoverableNode, visited):
    if root_node == first_node:
        first_node.discovered = True

    elif root_node == second_node:
        second_node.discovered = True

    if first_node.discovered and second_node.discovered:
        # We've discovered both nodes, yeah!
        return

    for neighbor in root_node.neighbors():
        if neighbor.key in visited:
            continue

        visited[neighbor.key] = root_node

        discover_path_to_nodes(neighbor, first_node, second_node, visited)


# Runtime of this function: O(n)
def is_node_descendent_of_give_node(descendent: DiscoverableNode, node: DiscoverableNode, visited):
    # Node is a descendent of a given node if there is a path from descentent to ascendent
    # Let's traverse and see if we can get from descendent to ascendent

    if descendent == node:
        return True

    while True:
        if descendent.key not in visited:
            break

        parent = visited[descendent.key]

        if parent == node:
            return True

        descendent = parent

    return False

# O(n)
def find_first_common_ancestor(root_node: DiscoverableNode, first_node: DiscoverableNode, second_node: DiscoverableNode, visited):
    if first_node.key not in visited:
        raise Exception("Failed to discover the first node from the root node!")

    elif second_node.key not in visited:
        raise Exception("Failed to discover the second node from the root node!")

    # Are both nodes on the left side? If so, then we are sure that the ancestor is on the LEFT side.

    if root_node.left_child:
        if is_node_descendent_of_give_node(first_node, root_node.left_child, visited) and is_node_descendent_of_give_node(second_node, root_node.left_child, visited):
            # Seems like both are on the left side. Let's dive deeper!
            return find_first_common_ancestor(root_node.left_child, first_node, second_node, visited)

    if root_node.right_child:
        if is_node_descendent_of_give_node(first_node, root_node.right_child, visited) and is_node_descendent_of_give_node(second_node, root_node.right_child, visited):
            return find_first_common_ancestor(root_node.right_child, first_node, second_node, visited)

    # Ok nodes are probably scattered (one is on left and another one is on right ...). Is the current node the ancestor
    # of them?

    if is_node_descendent_of_give_node(first_node, root_node, visited) and is_node_descendent_of_give_node(second_node, root_node, visited):
        return root_node

    # Well if we came so far, then there is no Ancestor between given nodes ... which is weird, yep
    raise ValueError("Node {} and {} dont have common ancestor!".format(first_node.key, second_node.key))


visited = {}

first_node = g
second_node = c

discover_path_to_nodes(a, first_node=first_node, second_node=second_node, visited=visited)

print(find_first_common_ancestor(a, first_node, second_node, visited).key)