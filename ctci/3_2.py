# Implement a Stack DS that also has a min() method, that returns the min. element of stack in O(1) time

# Idea: Besides the top element, we also track the mins

from ctci.common.classes import *


class StackWithMin2(Stack):
    def __init__(self):
        self.s2 = Stack()

        super().__init__()

    def min(self):
        if self.s2.empty():
            return None
        else:
            return self.s2.peek()

    def push(self, value):
        if self.min() is None or value <= self.min():
            self.s2.push(value)

        super().push(value)

    def pop(self):
        value = super().pop()

        if value == self.min():
            self.s2.pop()

        return value

s = StackWithMin2()

print("HERE SOMEHOW")

# s.push(5)
# s.push(10)
# s.push(15)
# s.push(3)

# while not s.empty():
#     print(s.min())
#
#     s.pop()