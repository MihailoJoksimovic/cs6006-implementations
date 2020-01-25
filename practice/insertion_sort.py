# 1. Implement insertion sort
# 2. Implement with binary search

from math import floor

def binary_search(array, element, start, end):
    """Find index of given element in array"""

    middle = floor((start + end) / 2)

    if array[middle] == element:
        return middle

    if start == end:
        return start if array[middle] > element else start + 1

    # If only one element's left --> compare to it and return the appropriate position
    if (end - start) == 1:
        return start if array[middle] > element else start + 1

    if array[middle] > element:
        # Element is to the left
        return binary_search(array, element, start, middle - 1)
    else:
        # Element is to the right
        return binary_search(array, element, middle + 1, end)

def insertion_sort(array):

    for i in range(1, len(array)):
        # If previous element is lower then current, then we dont do anything

        key = array[i]
        previous = array[i - 1]

        if previous < key:
            continue

        # Find index where to plug the element in

        new_index = binary_search(array, key, 0, i - 1)

        j = i - 1

        # Shift everything from new index to i, and then update i
        while j >= new_index and j >= 0:
            array[j + 1] = array[j]

            j -= 1

        array[new_index] = key

        # j = i - 1

        # while array[j] > key and j >= 0:
        #     # push forward as long as we are bigger :)
        #     array[j + 1] = array[j]
        #
        #     j -= 1

    print("Sorted array:")
    print(array)
    # return array

arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
expected = [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]

insertion_sort(arr)

# input = [5, 10, 20, 40]
# print(binary_search(input, 50, 0, len(input)))

# assert(insertion_sort(arr) == expected)