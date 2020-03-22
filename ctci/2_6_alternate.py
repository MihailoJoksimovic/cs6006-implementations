# Alternative solution to 2.6 --> what if we KNEW the list size?

from ctci.common.classes import *

list = SinglyLinkedList()

list.add(0).add(1).add(2).add(1).add(1)

list = SinglyLinkedList()
list.add("a").add("b").add("b").add("b")

def isPalindrome(head: ListNode):
    size = getSize(head)

    return isPalindromeRecurse(head, size).result

class Result:
    def __init__(self, result: bool, next: ListNode):
        self.result = result
        self.next = next

def isPalindromeRecurse(head: ListNode, size: int):
    if size <= 0:
        return Result(True, head)
    elif size == 1:
        return Result(True, head.next)

    result = isPalindromeRecurse(head.next, size - 2)

    if result.result is False:
        return result

    result.result = head.value == result.next.value

    result.next = result.next.next

    return result



def getSize(head: ListNode):
    size = 0

    while head is not None:
        size += 1

        head = head.next

    return size

if isPalindrome(list.head):
    print("List is palindrome!")
else:
    print("List is NOT palindrome!")

