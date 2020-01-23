from math import ceil

def _should_swap(left, right, reverse = False):
    """
    Returns true if left and right elements need to be swapped

    """

    return right >= left if reverse else right <= left

def insertion_sort(array, reverse = False):

    for i in range(1, len(array)):
        j = i - 1

        key = array[i]

        if not _should_swap(array[j], key, reverse):
            continue

        while j >= 0: # as long as the key is smaller then previous element, shift elements forward
            if not _should_swap(array[j], key, reverse):
                break

            array[j + 1] = array[j]

            j = j - 1

        array[j + 1] = key

    return array

def find_swap_index(array, key):
    """Finds an index where the swap needs to happen"""

    idx = None

    if len(array) == 1 and array[0] != key:
        return None

    # Find middle element
    if len(array) % 2 == 0:
        middleIdx = int(len(array) / 2)
    else:
        middleIdx = int((len(array) / 2) + 0.5)

    middleElement = array[middleIdx]

    if middleElement == key:
        return middleIdx

    if len(array) == 1:
        return None

    if middleElement > key:
        # We need to look on the LEFT side
        subArray = array[0:middleIdx]
    else:
        subArray = array[middleIdx:]

    return find_swap_index(subArray, key)

def binary_insertion_sort(array):
    """Uses binary search to find the element to sort by ..."""

    # We're starting from first element ...
    # for i in range(1, len(array)):


arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
expected = [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]

# print(insertion_sort(arr, True))
#
# print(insertion_sort(arr))
#
# print("Assertion went through! Good job!")

# print(find_swap_index([0, 1, 2, 3, 4], 100))

print(find_swap_index([0, 100], 100))