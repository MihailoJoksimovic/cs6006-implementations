# Task: Sort stack of numbers by using only one temporary Stack as a data struct. Nothing else is allowed.

from ctci.common.classes import *

class SortedStack(Stack):

    def __init__(self):
        # We'll use this one for sorting
        self.temp_stack = Stack()

        self.count = 0

        super().__init__()

    def push(self, value):
        self.count += 1

        if self.peek() is None or value > self.peek():
            # Insert on top if
            super().push(value)

            return

        # So the value seems to be lower than the top value
        # Let's move elements to temp. stack until we reach
        # element lower than the one being inserted. After that we'll return the elements

        while self.peek() is not None and self.peek() > value:
            self.temp_stack.push(self.pop())

        super().push(value)

        # Return elements back

        while not self.temp_stack.empty():
            self.push(self.temp_stack.pop())

    def pop(self):
        el = super().pop()

        if el is None:
            return None

        self.count -= 1

        return el

    def sort(self):
        # This solution is O(n ^ 2)
        # How to improve?

        count = self.count

        while count > 0:
            min = None

            for i in range(count):
                el = self.pop()

                if min is None:
                    min = el

                    continue

                if el < min:
                    self.temp_stack.push(min)

                    min = el
                else:
                    self.temp_stack.push(el)

            # Push minimial element to stack
            self.push(min)

            count -= 1

            # Push all elements from temp stack to current stack
            while not self.temp_stack.empty():
                self.push(self.temp_stack.pop())

        # At this point we are sorted ...

s = SortedStack()

s.push(15)
s.push(7)
s.push(30)
s.push(6)
s.push(100)
s.push(1)

# s.sort()

while not s.empty():
    print(s.pop())




