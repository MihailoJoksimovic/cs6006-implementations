class Node:
    def __init__(self, key, left_child = None, right_child = None, parent = None):
        self.right_child = right_child
        self.left_child = left_child
        self.parent = parent
        self.key = key

    def insert(self, value):
        if value == self.key:
            return self

        if value < self.key:
            if self.left_child is None:
                self.left_child = Node(value, None, None, self)

                return self.left_child
            else:
                return self.left_child.insert(value)

        if value > self.key:
            if self.right_child is None:
                self.right_child = Node(value, None, None, self)

                return self.right_child
            else:
                return self.right_child.insert(value)

class BinarySearchTree:
    def __init__(self, root_node = None):
        self.root_node = root_node

    def insert(self, value):
        if self.root_node is None:
            self.root_node = Node(value)

            return self.root_node

        return self.root_node.insert(value)