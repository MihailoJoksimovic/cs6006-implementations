# Implement a function to check if binary tree is a BST - is_bst()

# BST is if node's left child is lower and right higher than current node's value

from ctci.common.classes import Node


root_node = Node(20)
root_node.left_child = Node(10, Node(5, Node(3, Node(19))), Node(15))
root_node.right_child = Node(30)

def is_bst(node: Node, min_value = None, max_value = None):
    if min_value and node.key < min_value:
        return False

    if max_value and node.key > max_value:
        return False

    # Check left-child. Left-child has to constrain to having max value lower than current node's value

    if node.left_child:
        if not is_bst(node.left_child, min_value, node.key):
            return False

    # Right child has to be HIGHER than min. value (which is parent's value) and whatever was the previous max_value
    if node.right_child:
        if not is_bst(node.right_child, node.key, max_value):
            return False

    return True

print(is_bst(root_node))




