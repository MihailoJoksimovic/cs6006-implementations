# Task: implement tree structure and traversal functions

from __future__ import annotations

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child: Node):
        if child.value < self.value:
            if self.left is None:
                self.left = child
            else:
                self.left.insert(child)

        if child.value > self.value:
            if self.right is None:
                self.right = child
            else:
                self.right.insert(child)

        return self

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value

def visit(node: Node):
    print(node.getValue())

def in_order_traversal(root: Node):
    if root.getLeft():
        in_order_traversal(root.getLeft())

    visit(root)

    if root.getRight():
        in_order_traversal(root.getRight())

def pre_order_traversal(root: Node):
    visit(root)

    if root.getLeft():
        pre_order_traversal(root.getLeft())

    if root.getRight():
        pre_order_traversal(root.getRight())


head = Node(8)

head.insert(Node(4))
head.insert(Node(10))
head.insert(Node(2))
head.insert(Node(6))
head.insert(Node(20))

in_order_traversal(head)

print("")
print("")

pre_order_traversal(head)


