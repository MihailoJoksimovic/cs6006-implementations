# Sum lists: you have two numbers represented by linked lists, where each node contains a single digit. Digits are
# stored in REVERSE order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers
# and returns the sum as a linked list.

# Follow-up: suppose digits are stored in forward order. Repeat the above problem

# Input: 7 - 1 - 6 + 5 - 9 - 2
# Output: 2 - 1 - 9

from ctci.common.classes import *

def sum_nodes(a: ListNode, b: ListNode, previous_remainder: int):
    a_val = a.value if a else 0
    b_val = b.value if b else 0

    remainder = 0
    sum = a_val + b_val + previous_remainder

    if sum >= 10:
        remainder = 1
        sum -= 10

    return (sum, remainder)

list_a = SinglyLinkedList().add(7).add(1).add(6)
list_b = SinglyLinkedList().add(5).add(9).add(2)
list_results = SinglyLinkedList()

a = list_a.head
b = list_b.head
remainder = 0

while True:
    if a is None and b is None:
        break

    sum, remainder = sum_nodes(a, b, remainder)

    if list_results is None:
        list_results = Node(sum)
    else:
        list_results = list_results.add(sum)

    a = a.next if a else None
    b = b.next if b else None

for node in list_results.getiterator():
    print(node.value)
