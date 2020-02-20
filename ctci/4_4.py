# Implement a function to check if binary tree is balanced. For this task, being balanced means that heights of subtrees
# never differ by more than one.

# So, let's start with the following two functions to implement:

#   1. is_balanced(root_node) -- checks the heights of left and right node and returns TRUE if it's balanced
#   2. get_height(node)

# So what we really need to do is just to get the left and right heights for each node

from ctci.common.classes import *

values = [5, 15, 30, 1, 45, 32, 8, 99, 72, 100, 1000, 50]
# values = [5, 15, 30]

bt = BinarySearchTree()

for value in values:
    bt.insert(value)

total_function_calls = 0

def get_height(node: Node):
    global  total_function_calls

    left_height = 0
    right_height = 0

    total_function_calls += 1

    if node.left_child:
        left_height = get_height(node.left_child) + 1

    if node.right_child:
        right_height = get_height(node.right_child) + 1

    if abs(left_height - right_height) > 1:
        print("Disbalance found at node {}".format(node.key))
        raise ValueError()

    return max(left_height, right_height)

def is_balanced(node: Node):
    try:
        left_height = get_height(node.left_child)
        right_height = get_height(node.right_child)

        return True
    except ValueError:
        return False


print(is_balanced(bt.root_node))

bt = BinarySearchTree()

bt.insert(5)
bt.insert(1)
bt.insert(6)

# print(is_balanced(bt.root_node))

print(total_function_calls)