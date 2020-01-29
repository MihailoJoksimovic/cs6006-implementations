# 2.1 Write a code to remove duplicates from an unsorted singly linked list

from ctci.linked_lists import *

def remove_duplicates(sli: SinglyLinkedList):
    # Holds list of occurences of all elements we've seen so far
    occurences = {}

    previousNode = None
    currentNode = sli.head

    while True:
        if currentNode is None:
            return sli

        value = currentNode.getValue()

        if value in occurences:
            previousNode.next = currentNode.getNext()
            currentNode = currentNode.getNext()

            continue

        occurences[value] = True

        previousNode = currentNode
        currentNode = currentNode.getNext()

    return sli

def deduplicate_without_additional_data_structs(sli: SinglyLinkedList):
    """Removes duplicates without usage of hash table ... Uses two pointers to achieve this"""

    # This one iterates slowly (one element per full iteration of fast pointer)
    slowPointer = None

    # This one iterates fastly (i.e. all elements from slow one to the end
    fastPointer = None

    # Start at the head of the list
    slowPointer = sli.head
    fastPointer = slowPointer

    if sli.head.getNext() is None:
        # List has a single element ... returning the list as it is
        return sli

    fastPointer = slowPointer.getNext()

    while True:
        # This one iterates the slow pointer ...

        fastPointer = slowPointer

        while True:
            if fastPointer.getNext() is None:
                break

            if slowPointer.getValue() == fastPointer.getNext().getValue():
                if fastPointer.next.next:
                    fastPointer.next = fastPointer.next.next
                else:
                    fastPointer.next = None

            print("Slow: {}, Fast: {}".format(slowPointer.getValue(), fastPointer.getValue()))

            if fastPointer.getNext() is not None:
                fastPointer = fastPointer.getNext()
            else:
                break


        if slowPointer.getNext() is not None:
            slowPointer = slowPointer.getNext()
        else:
            break

head = Node(1)

head.addNext(Node(1)).addNext(Node(3)).addNext(Node(4)).addNext(Node(5)).addNext(Node(6)).addNext(Node(6))

sli = SinglyLinkedList(head)

# remove_duplicates(sli)
deduplicate_without_additional_data_structs(sli)

print_linked_list_elements(sli.head)