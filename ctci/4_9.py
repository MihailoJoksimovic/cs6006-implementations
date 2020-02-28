# BST sequences: a BST was created by traversing through array from left to right and inserting each element. Given a BST
# with distinct elements, print all possible arrays that could have lead to this tree

# NOTE for myself: current implementation doesnt consider all combinations of leafs ... blah

from ctci.common.classes import *

bst = BinarySearchTree()

# bst.insert(10)
# bst.insert(5)
# bst.insert(3)
# bst.insert(4)
# bst.insert(1)

bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(1)
bst.insert(6)
bst.insert(25)

# Idea: always start from root node

def dfs(node: Node, visited: list):
    # List of visited nodes
    visited.append(node.key)

    if node.left_child:
        dfs(node.left_child, visited)

    if node.right_child:
        dfs(node.right_child, visited)

    return visited

def get_permutations_of_two_2d_lists(a_lists, b_lists):
    """Returns all combinations of two lists"""

    combinations = []

    for list_a in a_lists:
        if len(b_lists) > 0:
            for list_b in b_lists:
                combinations.append(list_a + list_b)
        else:
            combinations.append(list_a)

    for list_b in b_lists:
        if len(a_lists) > 0:
            for list_a in a_lists:
                combinations.append(list_b + list_a)
        else:
            combinations.append(list_b)

    return combinations

def get_permutations(node: Node):
    permutations = []

    if node.is_leaf():
        return [[node.key]]

    # All permutations of left child
    left_child_permutations = []

    # All permutations of right child
    right_child_permutations = []

    if node.left_child:
        left_child_permutations = get_permutations(node.left_child)

    if node.right_child:
        right_child_permutations = get_permutations(node.right_child)

    # Now combine first with left children, then with right children

    for permutation in get_permutations_of_two_2d_lists(left_child_permutations, right_child_permutations):
        permutation = [node.key] + permutation

        permutations.append(permutation)

    return permutations

def weave_two_arrays(a, b, prefix: list):
    combinations = []

    if len(a) > 0:
        prefix.append(a.pop())

        combinations.extend(weave_two_arrays(a, b, prefix))

    if len(b) > 0:
        prefix.append(b.pop())

        combinations.extend(weave_two_arrays(a, b, prefix))
    pass



visited = []
print(get_permutations(bst.find(10)))

lists_a = [
    [5, 4, 3],
    [5, 3, 4]
]

lists_b = [
    [1, 2, 3, 4],
    [1, 3, 2, 4],
    [1, 3, 4, 2],
    [1, 4, 3, 2]
]

# print(get_permutations_of_two_2d_lists(lists_a, lists_b))

print(weave_two_arrays([1, 2], [3, 4]))