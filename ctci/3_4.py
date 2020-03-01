# Task: Implement Queue using Two stacks

# Idea: Move one stack to another and pop from another -- that's how we get a queue.
# Optimal solution: don't move back until needed

from ctci.common.classes import *

class QueueWithStacks:

    def __init__(self):
        # Stack used when adding elements
        self.insert_stack = Stack()

        # Stack used when popping the elements
        self.remove_stack = Stack()

    def add(self, value):
        # O(1)
        self.insert_stack.push(value)

    def get(self):
        """Return next item in queue"""

        # Worst-case: O(n) where n is total number of inserted elements

        if self.remove_stack.empty() and not self.insert_stack.empty():
            self.__from_a_to_b(self.insert_stack, self.remove_stack)

        return self.remove_stack.pop()

    def __from_a_to_b(self, stack_a: Stack, stack_b: Stack):
        """Moves all elements from stack A to stack B"""

        while not stack_a.empty():
            stack_b.push(stack_a.pop())


q = QueueWithStacks()

for i in range(1, 5):
    q.add(i)

for i in range(3):
    print(q.get())

for i in range(5, 10):
    q.add(i)

while True:
    el = q.get()

    if el is None:
        break

    print(el)