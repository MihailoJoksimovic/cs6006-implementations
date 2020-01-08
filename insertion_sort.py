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

arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
expected = [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]

print(insertion_sort(arr, True))

print(insertion_sort(arr))

print("Assertion went through! Good job!")