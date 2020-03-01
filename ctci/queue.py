# Idea: implement a Queue using pure Python. Queue is FIFO data structure

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None # type: QueueNode


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        new_node = QueueNode(value)

        if self.first is None:
            self.first = new_node

            self.last = new_node

            return

        self.last.next = new_node

        self.last = new_node

    def remove(self):
        if self.first is None:
            return None

        node = self.first

        self.first = node.next

        return node.value

    def empty(self):
        return self.first is None

q = Queue()

q.add(5)
q.add(10)
q.add(15)

while not q.empty():
    print(q.remove())