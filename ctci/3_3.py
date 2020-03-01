# Stack of plates -- implement a SetOfStacks class that has multiple stacks and each one of those has capacity. Once
# the stack is OVER capacity, you start a new Stack. Additionally, implement a popAt(index) method that pops from
# given stack

from ctci.common.classes import Stack, StackNode

class StackWithCapacity(Stack):
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.bottom = None

        super().__init__()

    def push(self, value):
        self.count += 1

        super().push(value)

        if self.bottom is None:
            self.bottom = self.top

    def pop(self):
        self.count -= 1

        return super().pop()

    def is_full(self):
        return self.count >= self.capacity

    def pop_last(self):
        element = self.bottom

        # Find the new bottom

        new_bottom = self.top

        while new_bottom.next and new_bottom.next.value != element.value:
            new_bottom = new_bottom.next

        self.bottom = new_bottom

        return element





class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        if len(self.stacks) == 0:
            self.stacks.append(StackWithCapacity(self.capacity))

        current_stack = self.stacks[len(self.stacks) - 1] # type: StackWithCapacity

        if current_stack.is_full():
            current_stack = StackWithCapacity(self.capacity)

            self.stacks.append(current_stack)

        current_stack.push(value)

    def pop(self):
        if len(self.stacks) == 0:
            return None

        current_stack = self.stacks[len(self.stacks) - 1] # type: StackWithCapacity

        element = current_stack.pop()

        if current_stack.empty():
            self.stacks.pop()

        return element

    def popAt(self, index):
        if not self.stacks[index]:
            return None

        element = self.stacks[index].pop()

        while (index + 1) < self.total_stacks() - 1:
            # Take from another stack ;)
            self.__left_shift(self.stacks[index], self.stacks[index + 1])

            index += 1

        return element

    def __left_shift(self, a_stack: StackWithCapacity, b_stack: StackWithCapacity):
        while not a_stack.is_full() and not b_stack.empty():
            a_stack.push(b_stack.pop_last())


    def total_stacks(self):
        return len(self.stacks)


ss = SetOfStacks(5)

for x in range(1, 15):
    ss.push(x)

print(ss.total_stacks())

print(ss.popAt(0))