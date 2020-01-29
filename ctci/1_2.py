# 1.2 Given two strings, check if one is permutation of another

# Permutation == equal number of all characters, right?

# One solution is to add chars and number of chars to hashmap,
# and then compare if they have same number of chars.

# Another solution is to treat letters as numbers really. Summing
# up the numbers should give the same result, right?

def is_permutation(a, b):
    # This runs in O(|a| + |b)) I'd argue ...
    # can we do better?

    sum_a = 0
    sum_b = 0

    for letter in a:
        sum_a += ord(letter)

    for letter in b:
        sum_b += ord(letter)

    return sum_a == sum_b

print(is_permutation("Mixa", "Xiam1"))
