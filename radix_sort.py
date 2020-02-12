from math import log10

def count_sort(arr, highest_number):
    counts = []

    for i in range(highest_number + 1):
        counts.append(0)

    for num in arr:
        counts[num] += 1

    for key, occurences in enumerate(counts):
        if occurences == 0:
            continue

        for i in range(occurences):
            print(key)

def count_sort_by_digit(array, digit_index):
    """Sorts the array based on the given digit index"""

    counts = []

    for i in range(10):
        counts.append([])

    for element in array:
        digit = extract_digit(element, digit_index)

        counts[digit].append(element)

    output = []

    for i in range(10):
        if len(counts[i]) == 0:
            continue

        for element in counts[i]:
            output.append(element)

    return output

def extract_digit(number, n, base = 10):
    """Extract n-th digit from number"""
    return (number // base ** n) % base

def find_highest_number_in_array(array):
    highest = None

    for i in array:
        if highest is None:
            highest = i
        elif highest < i:
            highest = i

    return highest

def radix_sort(array, base = 10):
    # Find highest number

    highest_number = find_highest_number_in_array(array)

    # https://math.stackexchange.com/questions/469606/how-to-get-count-of-digits-of-a-number
    highest_num_of_digits = int(log10(highest_number) + 1)

    # We want to iterate and sort by each digit, starting from least significant digit

    for digit_num in range(highest_num_of_digits):
        array = count_sort_by_digit(array, digit_num)

    return array




arr = [100, 10, 15, 10, 4, 0, 6, 17, 1000, 500, 300]
#
# count_sort(arr, 1000)

# print(extract_digit(85721, 3))

print(radix_sort(arr, 0))