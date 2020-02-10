from collections import deque

class Node:

    def __init__(self, value, parent = None):
        self.value = value

        self.parent = parent

        self.left = None
        self.right = None

    def height(self):
        if self.left_height() > self.right_height():
            return self.left_height()
        else:
            return self.right_height()

    def left_height(self):
        return self.left.height() + 1 if self.left else 0

    def right_height(self):
        return self.right.height() + 1 if self.right else 0

    def insert(self, value):
        if value == self.value:
            return

        if value < self.value:
            if self.left is None:
                self.left = Node(value, self)
            else:
                self.left.insert(value)

        if value > self.value:
            if self.right is None:
                self.right = Node(value, self)
            else:
                self.right.insert(value)

def visit(node: Node):
    print("Value: {}, Left: {}, Right: {}".format(node.value, node.left_height(), node.right_height()))


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

root = Node(50)

root.insert(40)
root.insert(60)
root.insert(45)
root.insert(35)

root.insert(65)
root.insert(66)
root.insert(55)

print_binary_search_tree(root)