# Return k-th to last -- use one fast pointer that goes k elements upfront. Once it reaches the end, we're on the right
# one

from ctci.linked_lists import *

head = Node(1)

sli = SinglyLinkedList(head)

for i in range(2, 10):
    head = head.addNext(Node(i))

def get_kth_to_last(sli: SinglyLinkedList, k: int):
    fast_p = sli.head
    slow_p = sli.head

    # Get fast pointer to proper position

    shifts = k

    for i in range(k - 1):
        fast_p = fast_p.next

        if fast_p is None:
            raise ValueError("The list has less than {} elements!".format(k))

    print("Fast pointer is at {}".format(fast_p.value))
    print(fast_p.value)

    # Ok now we have fast_p set to k elements in advance. Iterate until the fast_p reaches the end

    while True:
        fast_p = fast_p.next

        if fast_p is None:
            return slow_p

        slow_p = slow_p.next

    # That's it :)

def kth_to_last_recursive(node: Node, k: int):
    """Implements the k-th to last but using recursive approach. I honestly dislike this as it's completely unintuitive"""

    if node == None:
        return 0

    index = kth_to_last_recursive(node.next, k) + 1

    if index == k:
        print(node.value)

    return index

head = sli.head

while head is not None:
    print(head.value)

    head = head.next

print(get_kth_to_last(sli, 3).value)

kth_to_last_recursive(sli.head, 3)