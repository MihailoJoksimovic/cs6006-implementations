class Node:
    def __init__(self, label, weight):
        self.label = label
        self.weight = weight

class NodesPrioQueue:
    def __init__(self):
        self.values = []

    def parent(self, index):
        if index == 0:
            return None

        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def has_left_child(self, index):
        return self.left_child(index) < len(self.values)

    def right_child(self, index):
        return 2 * index + 2

    def has_right_child(self, index):
        return self.right_child(index) < len(self.values)

    def insert(self, node: Node):
        first_empty_slot = len(self.values)

        self.values.append(node)

        current_index = first_empty_slot

        while current_index > 0 and node.weight < self.values[self.parent(current_index)].weight:
            parent_value = self.values[self.parent(current_index)]

            self.values[self.parent(current_index)] = node
            self.values[current_index] = parent_value

            current_index = self.parent(current_index)

    def get_min_child(self, index):
        if self.has_left_child(index):
            left_child_index = self.left_child(index)

            if self.has_right_child(index):
                right_child_index = self.right_child(index)

                if self.values[left_child_index].weight < self.values[right_child_index].weight:
                    return left_child_index
                else:
                    return right_child_index
            else:
                return left_child_index

        if self.has_right_child(index):
            return self.right_child(index)

        return None

    def is_leaf(self, index):
        return self.has_left_child(index) or self.has_right_child(index)

    def getLowest(self):
        # Basically removes the top of the heap

        if len(self.values) == 0:
            return None

        to_return = self.values[0]

        # Take the last element and shift it to root

        if len(self.values) == 1:
            del self.values[0]

            return to_return

        last_element = self.values[len(self.values) - 1]

        del self.values[len(self.values) - 1]

        self.values[0] = last_element

        current_index = 0
        swap_index = None

        while True:
            swap_index = self.get_min_child(current_index)

            if swap_index is None:
                return to_return

            swap_el = self.values[swap_index]

            self.values[swap_index] = self.values[current_index]

            self.values[current_index] = swap_el

            current_index = swap_index

            if self.is_leaf(current_index):
                break

        return to_return

    def purge(self):
        self.values = []

if __name__ == "__main__":
    pq = NodesPrioQueue()

    pq.insert(Node("G", 10))
    pq.insert(Node("R", 1))

    print(pq.getLowest().label)
    print(pq.getLowest().label)