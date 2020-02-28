# Check if subtree: T1 and T2 are very large trees. Check if T2 is a subtree of T1. T2 is a subtree of T1 if all nodes
# from T2 match all nodes in T1

# Idea: First - find the root node of T2. if there's no root node of T2 present in T1, then they surely aren't identical

from ctci.common.classes import *

t1 = BinarySearchTree()
t2 = BinarySearchTree()

t2.root_node = Node(10, Node(4, None, Node(30)), Node(6))

t1.root_node = Node(
    26,
    t2.root_node,
    Node(
        3,
        None,
        Node(3)
    )
)



# First step -- find if T2's root node is present in T1.

matching_node = find_node_in_binary_tree(t1.root_node, t2.root_node.key)

if not matching_node:
    print("Trees are not the same!")

    exit()

# Complexity: O(|
def are_nodes_identical(node_1, node_2):
    if not node_1 or not node_2:
        return False

    if node_1.key != node_2.key:
        return False

    if node_1.left_child or node_2.left_child:
        if not are_nodes_identical(node_1.left_child, node_2.left_child):
            return False

    if node_1.right_child or node_2.right_child:
        if not are_nodes_identical(node_1.right_child, node_2.right_child):
            return False

    return True

if are_nodes_identical(matching_node, t2.root_node):
    print("Found T2 in T1")
else:
    print("T2 doesnt exist in T1")

