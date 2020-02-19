# Given a binary tree, design an algo. which creates a linked list of all the nodes at each depth (e.g. if you have a
# tree with depth D, you'll have D linked lists).

# Ok, so first to approach the problem logically. Assuming that we DO NOT know the depth in advance, we first have to
# figure it out. The only way to actually find out the depth is to do a depth first search, visit all nodes, and see
# what's the maximum level where the leafs are located.

# Actually no, we don't have to know it? We can just traverse and introduce the levels as we go down?

# Let's actually go with simple solution --> traverse the graph, mark each node and then derive the lists from it

class SinglyLinkedListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.first_node = None

    def prepend(self, value):
        if self.first_node is None:
            self.first_node = SinglyLinkedListNode(value)
        else:
            new_node = SinglyLinkedListNode(value, self.first_node)

            self.first_node = new_node

class Node:
    def __init__(self, key, left_child, right_child):
        self.right_child = right_child
        self.left_child = left_child
        self.key = key

    def insert(self, value):
        if value == self.key:
            return self

        if value < self.key:
            if self.left_child is None:
                self.left_child = Node(value, None, None)

                return self.left_child
            else:
                return self.left_child.insert(value)

        if value > self.key:
            if self.right_child is None:
                self.right_child = Node(value, None, None)

                return self.right_child
            else:
                return self.right_child.insert(value)


class BinarySearchTree:
    def __init__(self, root_node = None):
        self.root_node = root_node

    def insert(self, value):
        if self.root_node is None:
            self.root_node = Node(value, None, None)

            return self.root_node

        return self.root_node.insert(value)



values = [5, 15, 30, 1, 45, 32, 8, 99, 72, 100, 1000, 50]

bt = BinarySearchTree()

sll = SinglyLinkedList()

for value in values:
    bt.insert(value)
    sll.prepend(value)

# Now what we want to do ... we want to do a DFS and to tag each node with level to which it belongs

def dfs(node: Node, previous_level = -1):
    node.level = previous_level + 1

    node.height = 0

    if node.left_child:
        dfs(node.left_child, node.level)

    if node.right_child:
        dfs(node.right_child, node.level)

    if node.left_child or node.right_child:
        left_height = node.left_child.height if node.left_child else -1
        right_height = node.right_child.height if node.right_child else - 1

        node.height = max(left_height, right_height) + 1

def node_to_linked_list_node(node: Node, chain: SinglyLinkedList):
    chain.prepend(node.key)

    if node.left_child:
        node_to_linked_list_node(node.left_child, chain)

    if node.right_child:
        node_to_linked_list_node(node.right_child, chain)


def extract_nodes_at_depth(root_node: Node, depth):
    if root_node.level == depth:
        return [root_node]

    nodes = []

    if root_node.level != (depth - 1):
        return extract_nodes_at_depth()

    if root_node.level == (depth - 1):
        if root_node.left_child is not None:
            nodes.append(root_node.left_child)

        if root_node.right_child is not None:
            nodes.append(root_node.right_child)

    return nodes


def get_linked_list_from_given_depth(tree: BinarySearchTree, depth: int):
    # First, we need to figure out the depth of the tree, obviously
    dfs(tree.root_node)

    # Then, let's see if depth is bigger than the height of tree?

    if tree.root_node.height < depth:
        raise ValueError("Invalid depth {}. Tree goes to size of {}".format(depth, tree.root_node.height))

    nodes_at_given_depth = extract_nodes_at_depth(tree.root_node, depth)

    chain = SinglyLinkedList()

    for node in nodes_at_given_depth:
        node_to_linked_list_node(node, chain)

    return chain

b = get_linked_list_from_given_depth(bt, 3)

a = 1

