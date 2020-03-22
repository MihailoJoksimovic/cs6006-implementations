# Sum lists: you have two numbers represented by linked lists, where each node contains a single digit. Digits are
# stored in NORMAL order. Write a function that adds the two numbers and returns the sum as a linked list.

# Input: 6 - 1 - 7 + 2 - 9 - 5
# Output: 9 - 1 - 2

# NOTE: There is a bug when lists are not of equal length! This should be fixed with padding!

from ctci.common.classes import *

list_a = SinglyLinkedList().add(6).add(1).add(7)
list_b = SinglyLinkedList().add(2)
results = SinglyLinkedList()

def sum_nodes(a: ListNode, b: ListNode, remainders: SinglyLinkedList):
    a_val = a.value if a else 0
    b_val = b.value if b else 0

    sum = a_val + b_val

    if sum >= 10:
        remainders.add(1)

        sum -= 10
    else:
        remainders.add(0)

    return sum

a = list_a.head
b = list_b.head

# Do sums of two lists first and then iterate until we have remainders

remainders = SinglyLinkedList()

while True:
    if a is None and b is None:
        break

    sum = sum_nodes(a, b, remainders)

    results.add(sum)

    a = a.next if a else None
    b = b.next if b else None

# Remainders has to have one more element
remainders.add(0)

new_results = SinglyLinkedList()
new_results.add(remainders.head)

a = results.head
b = remainders.head.next

# Add remainders to the result
while True:
    if a is None and b is None:
        break

    sum = sum_nodes(a, b, SinglyLinkedList())

    new_results.add(sum)

    a = a.next if a else None
    b = b.next if b else None

for node in new_results.getiterator():
    print(node.value)