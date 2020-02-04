from collections import deque

class Node:

    def __init__(self, value, height = 0, parent = None, left = None, right = None):
        self.value = value
        self.height = height
        self.parent = parent
        self.left = left
        self.right = right

    def insert(self, value):
        if self.left is None and self.right is None:
            # So we just added one more level basically
            self.height += 1

            if self.parent and self.parent.height < (self.height + 1):
                # Well, parent's height needs to increase as well :)
                self.parent.height += 1

        if value < self.value:
            if self.left is None:
                self.left = Node(value, height = 0, parent=self)
            else:
                self.left.insert(value)

        if value > self.value:
            if self.right is None:
                self.right = Node(value, height = 0, parent=self)
            else:
                self.right.insert(value)

def visit(node: Node):
    print("Value: {}, Height: {}".format(node.value, node.height))


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