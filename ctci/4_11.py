# Implement a binary tree class that, along with insert(), find() and delete() has also a getRandomNode() method
# that returns a random node from the tree. Each node should be equally possible to be picked.

from random import randint

class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None # type: Node
        self.right_child = None # type: Node
        self.height = 0
        self.size = 0

    def insert(self, value):
        if value < self.key:
            if self.left_child is None:
                self.left_child = Node(value)
            else:
                self.left_child.insert(value)

        if value > self.key:
            if self.right_child is None:
                self.right_child = Node(value)
            else:
                self.right_child.insert(value)

        self.height = self.get_height()

        self.size += 1

    def find(self, value):
        if value == self.key:
            return self

        if value < self.key:
            if self.left_child is None:
                return None
            else:
                return self.left_child.find(value)

        if value > self.key:
            if self.right_child is None:
                return None
            else:
                return self.right_child.find(value)

    def get_height(self):
        if self.is_leaf():
            return 0
        else:
            left_height = self.left_child.get_height() if self.left_child else 0
            right_height = self.right_child.get_height() if self.right_child else 0

            return max(left_height, right_height) + 1

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

    def get_random(self):
        if self.size == 0:
            return self

        random_num = randint(0, self.size - 1)

        if random_num == 0:
            return self

        if self.left_child and random_num <= self.left_child.size:
            return self.left_child.get_random()

        return self.right_child.get_random()





node = Node(50)

node.insert(70)
node.insert(40)
node.insert(35)
node.insert(25)

a = 5

for i in range(0, 15):
    print(node.get_random().key)
