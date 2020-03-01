# Idea: Implement a Stack data structure

class StackNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next # type: StackNode

class Stack:
    def __init__(self):
        self.top = None # type: StackNode

    def push(self, value):
        new_node = StackNode(value)

        if self.top:
            new_node.next = self.top

        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        next_top = self.top.next

        top = self.top

        self.top = next_top

        return top.value

    def peek(self):
        return self.top.value if self.top else None

    def empty(self):
        return self.top is None

s = Stack()

s.push(5)
s.push(10)
s.push(15)

while not s.empty():
    print(s.pop())

print(s.pop())