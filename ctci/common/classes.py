from queue import Queue

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

    def has_at_least_one_child(self):
        return self.left_child is not None or self.right_child is not None

    def has_both_childs(self):
        return self.left_child is not None and self.right_child is not None

    def is_leaf(self):
        return not self.has_at_least_one_child()

    def find(self, value):
        if value == self.key:
            return self

        if value < self.key:
            if self.left_child:
                return self.left_child.find(value)
            else:
                return None

        if value > self.key:
            if self.right_child:
                return self.right_child.find(value)
            else:
                return None

        return None


class BinarySearchTree:
    def __init__(self, root_node = None):
        self.root_node = root_node

    def insert(self, value):
        if self.root_node is None:
            self.root_node = Node(value)

            return self.root_node

        return self.root_node.insert(value)

    def find(self, value):
        return self.root_node.find(value)


def visit(node: Node):
    print(node.key)


def in_order_traversal(node: Node):
    if node.left_child:
        in_order_traversal(node.left_child)

    visit(node)

    if node.right_child:
        in_order_traversal(node.right_child)


def pre_order_traversal(node: Node):
    visit(node)

    if node.left_child:
        pre_order_traversal(node.left_child)

    if node.right_child:
        pre_order_traversal(node.right_child)


def post_order_traversal(node: Node):
    if node.right_child:
        post_order_traversal(node.right_child)

    visit(node)

    if node.left_child:
        post_order_traversal(node.left_child)


def find_node_in_binary_tree(root_node: Node, value):
    """Does a BFS search to find the matching value ..."""

    frontier = Queue()

    frontier.put(root_node)

    while not frontier.empty():
        node = frontier.get()

        if node.key == value:
            return node

        if node.left_child:
            frontier.put(node.left_child)

        if node.right_child:
            frontier.put(node.right_child)

    return None


def array_to_binary_tree(array: list):
    """Builds a binary tree out of given list"""

    root_node = Node(array[0])

    array = array[1:]

    queue = Queue()

    queue.put(root_node)

    current_node = root_node

    while not queue.empty():

        if current_node.left_child is not None and current_node.right_child is not None:
            current_node = queue.get()

            if current_node == root_node:
                continue

        if len(array) == 0:
            break

        element = array[0]

        array = array[1:]

        if current_node.left_child is None:
            current_node.left_child = Node(element)

            queue.put(current_node.left_child)

            continue

        if current_node.right_child is None:
            current_node.right_child = Node(element)

            queue.put(current_node.right_child)

            continue

    return root_node



