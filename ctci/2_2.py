# 2.2 Return kth to last element of singly linked list

from ctci.linked_lists import *

def get_kth_element(sll: SinglyLinkedList, k):
    # First we need to iterate to get a size of the list ...

    if sll.head is None:
        raise ValueError("Linked list is empty")

    if sll.head.getNext() is None and k > 0:
        raise ValueError("Linked list has one element but k is: {}".format(k))

    # Iterate through list to get a size of it. Then we can get the k-th element

    totalNodes = 1
    currentNode = sll.head

    while True:
        if currentNode.getNext() is None:
            break

        totalNodes += 1

        currentNode = currentNode.getNext()

    print("List has total of: {} nodes".format(totalNodes))

    # Now we need to get to k-th before last

    total_iterations = totalNodes - k

    if totalNodes < 0:
        raise ValueError("Invalid k ({}) specified! List has only {} nodes".format(k, totalNodes))

    currentNode = sll.head

    for i in range(0, total_iterations):
        currentNode = currentNode.getNext()

    return currentNode

head = Node(1)

head.addNext(Node(1)).addNext(Node(3)).addNext(Node(4)).addNext(Node(5)).addNext(Node(6)).addNext(Node(6))

sll = SinglyLinkedList(head)

print(get_kth_element(sll, 0).getValue())

# print_linked_list_elements(sll.head)
