# Design an algo. to find a first common ancestor of two nodes in a binary tree (NOTE: this tree IS NOT a binary search tree!)
# Avoid storing additional nodes in a Data Structure

# In this solution, we're going to assume that nodes have links to parents.

from ctci.common.classes import *

class DiscoverableNode(Node):
    def __init__(self, key, left_child = None, right_child = None, parent = None):
        super().__init__(key, left_child, right_child, parent)

        if left_child:
            left_child.parent = self

        if right_child:
            right_child.parent = self

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

# O(deepest node)
def find_common_ancestor(p: DiscoverableNode, q: DiscoverableNode):
    """Finds the common ancestor for nodes p & q"""

    # Basically, what we're going to do is traverse up until nodes meet.
    # However, we must make sure that we start traversing up from the proper depth.
    # So we'll get depths for both nodes, and start going upwards from the deeper one, until we meet with both.

    p_depth = depth(p)
    q_depth = depth(q)

    # We go up until nodes collide at some point

    current_p = p
    current_q = q

    while True:
        if current_p is None and current_q is None:
            # Well we went all the way up and didnt find ancestors ...
            return None

        if current_p == current_q:
            # We found a common ancestor
            return current_p

        if p_depth == q_depth:
            # Move both up one node
            current_p = current_p.parent if current_p.parent else None
            current_q = current_q.parent if current_q.parent else None

            continue

        if p_depth > q_depth:
            # Move only P upwards
            current_p = current_p.parent

            p_depth -= 1
        else:
            # Move only Q upwards
            current_q = current_q.parent

            q_depth -= 1


def depth(node: Node):
    # Depth is defined as --> we traverse up until there's no more parents :)

    depth = 0

    current_node = node

    while current_node.parent:
        depth += 1

        current_node = current_node.parent

    return depth

print(find_common_ancestor(g, b).key)


