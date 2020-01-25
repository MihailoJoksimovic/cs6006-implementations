from math import floor

def split(array, start, end):
    if len(array) < 2:
        raise ValueError("Trying to split array with one element! Doesnt make sense!")

    if (end - start) == 1:
        return start, start, end, end

    # Left starts at beginning anyway
    left_start = start

    # Right always end in the end
    right_end = end

    left_end = ((start + end) // 2) - 1
    right_start = left_end + 1

    return left_start, left_end, right_start, right_end

def merge(array, left_start, left_end, right_start, right_end):
    if left_start != left_end:
        # Left side has more elements, split and do a recursive merge
        new_left_start, new_left_end, new_right_start, new_right_end = split(array,left_start, left_end)

        merge(array, new_left_start, new_left_end, new_right_start, new_right_end)

    if right_start != right_end:
        # Right side has more elements, split and do a recursive merge
        new_left_start, new_left_end, new_right_start, new_right_end = split(array, right_start, right_end)

        merge(array, new_left_start, new_left_end, new_right_start, new_right_end)


    # Ok it's guaranteed now that our arrays are properly sorted. We can merge them now ;)

    left_index = left_start
    right_index = right_start

    while left_index <= left_end and right_index <= right_end:
        if array[left_index] < array[right_index]:
            # All good, just increase the left index
            left_index += 1

            continue

        if array[left_index] > array[right_index]:
            right_element = array[right_index]

            # Shift all elements to the right
            j = right_index

            while j > left_index:
                array[j] = array[j - 1]

                j -= 1

            # Do actual swap
            array[left_index] = right_element

            # Sort out the indexes etc.
            left_index += 1
            left_end += 1
            right_index += 1

    return array

arr = [100, 10, 15, 4, 0, 6, 17, 1000, 500, 300]

l_start, l_end, r_start, r_end = split(arr, 0, len(arr) - 1)

print(l_start, l_end)
print(r_start, r_end)

print(arr[l_start:l_end + 1])
print(arr[r_start:r_end + 1])

print(merge(arr, l_start, l_end, r_start, r_end))

# arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]


# print(merge_sort(arr))
