# Sum of paths: YOu are given a BINARY TREE in which each node has a number. Find all paths that sum to the given integer.
# Note: paths dont have to start at ROOT node and it doesnt have to end in leaf, but it has to travel downward.

from ctci.common.classes import *

bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(20)

find_node_in_binary_tree(bst.root_node, 5).insert(3)
find_node_in_binary_tree(bst.root_node, 5).insert(15)
find_node_in_binary_tree(bst.root_node, 20).insert(4)
find_node_in_binary_tree(bst.root_node, 20).insert(27)
find_node_in_binary_tree(bst.root_node, 3).insert(1)
find_node_in_binary_tree(bst.root_node, 3).insert(26)
find_node_in_binary_tree(bst.root_node, 4).right_child = Node(6)

def iter_nodes(root_node: Node):
    """Iterates through all nodes reachable from given node"""

    yield root_node

    if root_node.left_child:
        yield from iter_nodes(root_node.left_child)

    if root_node.right_child:
        yield from iter_nodes(root_node.right_child)

    return

target_value = 30
total_paths = 0

paths_leading_to_sum = []

def dfs_until_sum(node, current_sum: int, target_sum: int, current_path: list):
    if (node.key + current_sum) == target_sum:
        print("\tFound full sum at node: {}".format(node.key))

        paths_leading_to_sum.append(current_path + [node])

        return

    if (node.key + current_sum) > target_sum:
        # If we are above target sum at this point, there's no need to dig any deeper
        return

    if node.left_child:
        dfs_until_sum(node.left_child, node.key + current_sum, target_sum, current_path + [node])

    if node.right_child:
        dfs_until_sum(node.right_child, node.key + current_sum, target_sum, current_path + [node])

    return


for node in iter_nodes(bst.root_node):
    print("Starting iteration at node: {}".format(node.key))

    if node.key == target_value:
        print("Found full path at node: {}".format(node.key))

    if node.left_child:
        dfs_until_sum(node.left_child, node.key, target_value, [node])

    if node.right_child:
        dfs_until_sum(node.right_child, node.key, target_value, [node])


print("Total paths leading to {}: {}".format(target_value, len(paths_leading_to_sum)))