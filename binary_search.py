from math import floor

def binary_search(array, element, low, high):
    if low == high:
        return low if element < array[low] else low + 1

    if low > high:
        # We hit the leftmost barrier
        return low if element < array[low] else low + 1

    middle = floor((low + high) / 2)

    if element > array[middle]:
        return binary_search(array, element, middle + 1, len(array) - middle)
    else:
        return binary_search(array, element, low, middle - 1)

# total_iterations = 0

arr = [0, 4, 8, 10, 12, 18]
# print(binary_search(arr, 18, 0, len(arr) - 1))
# print("Total iterations: {}".format(total_iterations))

arr = [5, 10, 20, 30]
arr = [5, 10, 20, 30, 50]
print(binary_search(arr, 40, 0, len(arr) - 1))