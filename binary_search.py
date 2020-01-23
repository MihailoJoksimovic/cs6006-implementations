from math import floor

def binary_search(array, element, low, high):
    if low == high:
        return low if element < array[low] else low + 1

    if low > high:
        # We hit the leftmost barrier
        return low if element < array[low] else low + 1

    middle = floor((low + high) / 2)

    if element > array[middle]:
        return binary_search(array, element, middle + 1, high)
    else:
        return binary_search(array, element, low, middle - 1)

def insertion_sort(array, element):
    insert_idx = binary_search(array, element, 0, len(array) - 1)

    # Just append last element to the end so that elements are properly shifted
    array.append(array[len(array) - 1])

    for i in range(len(array) - 1, insert_idx, -1):
        array[i] = array[i - 1]

    array[insert_idx] = element

    return array


# total_iterations = 0

arr = [0, 4, 8, 10, 12, 18]
# print(binary_search(arr, 18, 0, len(arr) - 1))
# print("Total iterations: {}".format(total_iterations))

arr = [5, 10, 20, 30]
arr = [5, 10, 20, 30, 50]
# arr = [5, 10]
print(binary_search(arr, 70, 0, len(arr) - 1))

print(insertion_sort(arr, 25))