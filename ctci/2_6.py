# Implement a function to check if a linked list is a palindrome

# 1. Solution with a stack -- iterate through linked list and build a stack.
#   then iterate again and pop items from stack and compare

from ctci.common.classes import *

list = SinglyLinkedList()

list.add("a")
list.add("n")
list.add("a")
list.add("v")
list.add("o")
list.add("l")
list.add("i")
list.add("m")
list.add("i")
list.add("l")
list.add("o")
list.add("v")
list.add("a")
list.add("n")
list.add("a")

s = Stack()

for el in list.getiterator():
    s.push(el.value)

all_match = True

for el in list.getiterator():
    stack_el = s.pop()

    if el.value != stack_el:
        all_match = False
        break

if all_match:
    print("List is palindrome!")
else:
    print("List is NOT palindrome!")