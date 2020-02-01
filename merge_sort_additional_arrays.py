# Task: implement a merge sort with additional arrays for left and right ...

def split(array):
    """Splits array into two halves and returns left and right half"""

    if len(array) < 2:
        raise ValueError("Cant split array with less than 2 values!")

    middle = len(array) // 2

    left = array[0:middle]
    right = array[middle:]

    return left, right

def merge(left, right):
    if len(left) > 1:
        # Split left into two arrays and do a merge on those
        left_left, left_right = split(left)

        left = merge(left_left, left_right)

    if len(right) > 1:
        # Split right into two arrays and do a merge on those
        right_left, right_right = split(right)

        right = merge(right_left, right_right)

    # Now merge :)

    left_index = 0
    right_index = 0

    new_array = []

    while True:
        # Stop when left or right indexes go over the size of their respective arrays
        if left_index >= len(left) or right_index >= len(right):
            break

        if left[left_index] < right[right_index]:
            new_array.append(left[left_index])

            left_index += 1
        else:
            new_array.append(right[right_index])

            right_index += 1

    # Add remaining elements ...

    # Iterate left to the end ...
    while left_index < len(left):
        new_array.append(left[left_index])

        left_index += 1

    while right_index < len(right):
        new_array.append(right[right_index])

        right_index += 1

    return new_array

arr = [100, 10, 15, 4, 0, 6, 17, 1000, 500, 300, 400, 700, 1000]

left,right = split(arr)

print(merge(left, right))
