def root_of_heap(array):
    return 0

def parent_of_element(i, array):
    """Returns parent of element at i-th index"""
    return i // 2

def left_child_of_element(i, array):
    """Returns left child of i-th element"""

    return 2 * i + 1

def right_child_of_element(i, array):
    """Returns right child of i-th element"""

    return 2 * i + 2

def max_heapify(i, array):
    """Correct a single violation of the heap property in a subtree at its root"""

    l = left_child_of_element(i, array)
    r = right_child_of_element(i, array)

    largest = i

    if l < len(array) and array[l] > array[i]:
        largest = l

    if r < len(array) and array[r] > array[largest]:
        largest = r

    if largest != i:
        # Exchange largest and current
        temp = array[i]

        array[i] = array[largest]

        array[largest] = temp

        # Max heapify largest
        max_heapify(largest, array)

def build_max_heap(array):
    for i in range(len(array) // 2, -1, -1):
        max_heapify(i, array)


arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

print(left_child_of_element(3, arr))
print(right_child_of_element(3, arr))

arr2 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

# max_heapify(1, arr2)

build_max_heap(arr2)
print(arr2)

