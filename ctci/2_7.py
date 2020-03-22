# Intersection: find if two linked lists intersect. Intersection is defined by REFERENCE and not by VALUE.
# If they intersect - find intersection point.

# Algo: two lists intersect if the last element is the same. Therefore, iterate to end of both lists and make sure to
# save the lengths of each. If the last element is the same, then they intersect.
# If they intersect, move pointer to start of both, and from the longer one, just skip the first DIFFERENCE nodes, because
# it surely doesnt intersect there ...

from ctci.common.classes import *

list1 = SinglyLinkedList()
list1.add(1).add(2).add(3)

node_3 = list1.tail

list1.add(4).add(5).add(6)

list2 = SinglyLinkedList()
list2.add(8)

list2.tail.next = node_3

last_1 = None
last_2 = None

size_1 = 0
size_2 = 0

n1 = list1.head

while n1 is not None:
    last_1 = n1

    size_1 += 1

    n1 = n1.next

n2 = list2.head

while n2 is not None:
    last_2 = n2

    size_2 += 1

    n2 = n2.next

if last_1.__hash__() == last_2.__hash__():
    print("Lists intersect!")
else:
    print("No intersection!")

longer = list1.head if size_1 > size_2 else list2.head
shorter = list2.headafaa if size_1 > size_2 else list1.head

# Skip first X in longer list
for i in range(abs(size_1 - size_2)):
    longer = longer.next

p_1 = longer
p_2 = shorter

while True:
    if p_1.__hash__() == p_2.__hash__():
        print("Found intersection node: {}".format(p_1.value))

        break

    p_1 = p_1.next
    p_2 = p_2.next
