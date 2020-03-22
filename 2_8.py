# Loop detecion: detect if linked list has a cycle. Cycle happens if some node points back to a node that was already
# visited before.

# Approach: Fast runner, slow runner. Fast one moves twice as fast as slow one. eventually they will meet. Once they do,
# return slow to beginning of list, and iterate until they meet.

from ctci.common.classes import *

li = SinglyLinkedList()

li.add(1).add(2).add(3)

node_3 = li.tail

li.add(4).add(5)

li.tail.next = node_3

slow = li.head
fast = li.head.next.next

while True:
    if fast is None:
        break

    if slow == fast:
        # Found collision point
        break

    slow = slow.next

    if fast.next is None:
        break

    fast = fast.next.next

if slow != fast:
    print("No loop!")
    exit()

print("Woop! we have cycle!")

# Now that we have a loop -- move slow to beginning of list and loop until they meet

slow = li.head

while True:
    if slow == fast:
        break

    slow = slow.next
    fast = fast.next.next

print("Collision point: {}".format(slow.value))

