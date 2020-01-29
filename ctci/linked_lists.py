# I want to just create a linked list here ...

from __future__ import annotations

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def addNext(self, node):
        self.next = node
        return node

    def removeNext(self, node):
        self.next = None
        return self

    def getNext(self) -> Node:
        return self.next

    def getValue(self):
        return self.value

class SinglyLinkedList:

    def __init__(self, head: Node):
        self.head = head

def print_linked_list_elements(node: Node):
    nextNode = node

    print(nextNode.getValue())

    while nextNode.getNext():
        nextNode = nextNode.getNext()

        print(nextNode.getValue())

if __name__ == '__main__':
    head = Node(55)

    head.addNext(Node(33)).addNext(Node(21))

    nextNode = head

    print(nextNode.getValue())

    while nextNode.getNext():
        nextNode = nextNode.getNext()

        print(nextNode.getValue())