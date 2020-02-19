# Given an array of increasingly sorted integers with unique integer elements, implement algo. to create a BST with
# smallest height

# Idea 1: Set n // 2 to be the root
# Idea 2: Introduce a function build_tree that given the array of elements, returns a tree. The way it should work is --
#   if there is only ONE element in array - return it as a node. If there are two elements -- make a tree out of them.
#   If there are more than two --> split them further and recombine.

class Node:
    def __init__(self, key, left_child, right_child):
        self.right_child = right_child
        self.left_child = left_child
        self.key = key



def build_tree(elements):
    if len(elements) == 1:
        return Node(elements[0], None, None)

    if len(elements) == 2:
        return Node(elements[0], left_child = None, right_child = elements[1])

    # Pick a root

    n = len(elements)

    root = elements[n // 2]

    left = elements[:(n // 2)]
    right = elements[(n // 2 + 1):]

    return Node(root, left_child = build_tree(left), right_child = build_tree(right))

def build_min_tree(elements):
    return build_tree(elements)


elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tree = build_min_tree(elements)

a = 5