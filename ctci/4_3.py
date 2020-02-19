# Given a binary tree, design an algo. which creates a linked list of all the nodes at each depth (e.g. if you have a
# tree with depth D, you'll have D linked lists).

# So, the battle plan is: store linked list for each level in a dictionary (maybe we can reduce this actually?)? Maybe
# we can store only the index of last element in the dict? But let's see.

# Second thing is, we will create a function that, given a node, creates a linked list out of all of its child nodes
# Lets call this function root_node_to_linked_list()

# Finally, we will iterate the tree, level by level, and call root_node_to_linked_list() on each level

# Ok turns out that I misread this task :) It seems that it should have created linked lists with nodes only on CERTAIN
# level, not all nodes from that level downward .... Blah :)

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
# values = [5, 15, 30]

bt = BinarySearchTree()

sll = SinglyLinkedList()

for value in values:
    bt.insert(value)

def root_node_to_linked_list(root_node: Node, chain):
    chain.prepend(root_node.key)

    if root_node.left_child:
        root_node_to_linked_list(root_node.left_child, chain)

    if root_node.right_child:
        root_node_to_linked_list(root_node.right_child, chain)

    return chain


def binary_tree_to_linked_lists(root_node: Node, level, linked_lists_dict):
    # How many recursion levels do we have here? O(|V|) in total. I think it's actually O(3 * |V|) but we can round it
    # to O(|V|).

    # I think total complexity is O(|V| ^ 2)

    if level not in linked_lists_dict:
        linked_lists_dict[level] = SinglyLinkedList()

    # O(|V| * |V|)
    root_node_to_linked_list(root_node, linked_lists_dict[level])

    # Let's go one level deeper ...

    if root_node.left_child:
        # O(|V|) here
        binary_tree_to_linked_lists(root_node.left_child, level + 1, linked_lists_dict)

    if root_node.right_child:
        # O(|V|) here
        binary_tree_to_linked_lists(root_node.right_child, level + 1, linked_lists_dict)

    return linked_lists_dict


di = binary_tree_to_linked_lists(bt.root_node, level = 0, linked_lists_dict={})

b = 5