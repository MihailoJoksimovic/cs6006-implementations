# Write an algo. to find a successor of a given node in a Binary Search Tree (i.e. in-order traversal).
# You may assume that each node has link to its parent

# So what we need to do is traverse until we find the searched node. Once we find it, we need to find
# leftmost child of rightmost tree .... Fuck me :)

# So idea: once we hit the searched node, we can start storing the min. values that we encounter. Once we hit a value
# that is higher than min. value, we stop

from ctci.common.classes import *

bst = BinarySearchTree()

bst.insert(20)
bst.insert(10)
bst.insert(5)
bst.insert(8)
bst.insert(6)
bst.insert(7)

def find_inorder_successor(value, root_node: Node):
    pass

def visit(node: Node):
    print(node.key)

class Marker:
    def __init__(self):
        self.required_node_found = False
        self.min_value_encountered = None

def inorder_traversal_with_marker(searched_value, node: Node, marker: Marker):
    """This solution relies on existence of Marker class that shares the behavior. However, I understand that what is
    required is some other approach :)"""

    if node.left_child:
        inorder_traversal_with_marker(searched_value, node.left_child, marker)

    if marker.required_node_found:
        if marker.min_value_encountered is None:
            marker.min_value_encountered = node.key
        elif marker.min_value_encountered < node.key:
            return marker.min_value_encountered

    if node.key == searched_value:
        marker.required_node_found = True

    if node.right_child:
        inorder_traversal_with_marker(searched_value, node.right_child, marker)

def find_node(searched_value, root_node: Node):
    # Finds a given node

    if root_node.key == searched_value:
        return root_node

    if root_node.key > searched_value and root_node.left_child:
        return find_node(searched_value, root_node.left_child)
    elif root_node.key < searched_value and root_node.right_child:
        return find_node(searched_value, root_node.right_child)

    return None

def inorder_traversal_until_first_node(node: Node, value):
    if node.left_child and node.left_child.key != value:
        return inorder_traversal_until_first_node(node.left_child, value)

    return node.key

def inorder_search_for_successor(node: Node):
    # Search for successor. It should be the leftmost branch of right child. However, if there's no right child, we need
    # to go to parent and do from there

    if node.right_child:
        return inorder_traversal_until_first_node(node.right_child, node.key)

    return inorder_traversal_until_first_node(node.parent, node.key)


# print(find_successor_of(20, bst.root_node))

# print(inorder_traversal_with_marker(4, bst.root_node, Marker()))
# print(inorder_traversal_with_marker(8, bst.root_node, Marker()))

# First step --> find the node we are searching for
node = find_node(6, bst.root_node)

# Second step --> find the successor. Now note --> if there is no RIGHT branch, then we return the parent actually
print(inorder_search_for_successor(node))

a = 5
