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
        print("Inserting {}".format(value))

        new_node = None

        if value == self.value:
            return

        if value < self.value:
            if self.left is None:
                self.left = Node(value, self)

                new_node = self.left
            else:
                new_node = self.left.insert(value)

        if value > self.value:
            if self.right is None:
                self.right = Node(value, self)

                new_node = self.right
            else:
                new_node = self.right.insert(value)

        if self.parent:
            walk_up_and_check_for_disbalance(self.parent)

        return new_node

    def left_rotate(self):
        """
        Does a left rotation on the node
        Left-rotation takes the RIGHT CHILD (y), places it as a PARENT of current node,
        and takes y's LEFT child and makes it x's right child.
        """

        y = self.right

        y.parent = self.parent

        self.parent = y

        self.right = y.left

        y.left = self

    def right_rotate(self):
        """
        Does a right rotation on the node.

        Right-rotation takes the LEFT child of the node (x), makes it parent of current node,
        takes x's RIGHT CHILD and makes it y's left child
        :return:
        """

        x = self.left

        x.parent = self.parent

        if self.parent.left == self:
            self.parent.left = x
        else:
            self.parent.right = x

        self.left = x.right

        self.parent = x

        x.right = self






def walk_up_and_check_for_disbalance(node: Node):
    if abs(node.left_height() - node.right_height()) > 1:
        print("Node: {} needs rebalancing! Left: {}, Right: {}".format(node.value, node.left_height(), node.right_height()))

def visit(node: Node):
    print(
        "Value: {}, Parent: {}, Left height: {}, Left child: {}, Right height: {}, Right child: {}".format(
            node.value,
            node.parent.value if node.parent else "-",
            node.left_height(),
            node.left.value if node.left else "-",
            node.right_height(),
            node.right.value if node.right else "-"
        ),
    )


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

root = Node(41)

root.insert(20)
root.insert(65)
root.insert(11)
node_29 = root.insert(29)

root.insert(50)
root.insert(26)
root.insert(23)


print_binary_search_tree(root)

node_29.right_rotate()

print("After right rotation: ")

print_binary_search_tree(root)