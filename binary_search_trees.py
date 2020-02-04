from collections import deque


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = None


def insert(value, root: Node = None):
    """Inserts a new VALUE into a tree"""

    new_node = Node(value)

    if root is None:
        root = new_node

        return root

    if value < root.value:
        if root.left is None:
            root.left = new_node
        else:
            new_node = insert(value, root.left)

    if value > root.value:
        if root.right is None:
            root.right = new_node
        else:
            new_node = insert(value, root.right)

    return new_node


def search(value, root: Node):
    """Search for a value in binary tree"""

    if value == root.value:
        return root


    if value < root.value:
        if root.left is not None:
            return search(value, root.left)
        else:
            return None

    if value > root.value:
        if root.right is not None:
            return search(value, root.right)
        else:
            return None


def visit(node: Node):
    print(node.value)


def print_binary_search_tree(root: Node):
    """Prints the binary search tree by printing level-by-level"""

    queue = deque()

    queue.append(root)

    while queue:

        node: Node = queue.popleft()

        visit(node)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


root = insert(49, root)

insert(79, root)
insert(46, root)
insert(41, root)
insert(42, root)
insert(39, root)
insert(64, root)

print_binary_search_tree(root)

print("Doing search!")
print(search(64, root))
