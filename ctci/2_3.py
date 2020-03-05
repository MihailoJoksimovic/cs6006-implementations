# Delete middle node -- implement an algo. to remove the node from the linked list, given only access to that node

# Solution: just copy the elements from right to left

from ctci.linked_lists import *

head = Node("a")

b = head.addNext(Node("b"))

node_c = b.addNext(Node("c"))

node_c.addNext(Node("d")).addNext(Node("e")).addNext(Node("f"))

def wipe_out_node(node: Node):
    # Iterate through list and replace node with a next one

    previous = None

    while True:
        if not node.next:
            previous.next = None

            break

        node.value = node.next.value

        previous = node

        node = node.next

        if node is None:
            break

wipe_out_node(node_c)

while True:
    print(head.value)

    head = head.next

    if head is None:
        break
