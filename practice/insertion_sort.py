# 1. Implement insertion sort
# 2. Implement with binary search

def insertion_sort(array):

    for i in range(1, len(array)):
        # If previous element is lower then current, then we dont do anything

        key = array[i]
        previous = array[i - 1]

        if previous < key:
            continue

        j = i - 1

        while array[j] > key and j >= 0:
            # push forward as long as we are bigger :)
            array[j + 1] = array[j]

            j -= 1

        array[j + 1] = key

    # return array

arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
expected = [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]

insertion_sort(arr)

# assert(insertion_sort(arr) == expected)