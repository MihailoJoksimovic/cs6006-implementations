# Idea: have an array and always convert keys to array indexes
# How do we convert non-integer to positive integer? Prehashing!

# __hash__ on an object can be implemented on any object and it tells python
# how to hash the object. If you dont have it, it uses "id" property which is
# the physical location of the object in RAM

# Another problem: huge memory space required. Solution: hashing()!
# Hashing refers to process of cutting stuff into smaller pieces, then mixing
# them up

# Idea of hashing --> take universe (U) of all possible keys and reduce to small set
# of possible integers (m). Ideally, m should be around "n" (i.e. should be similar
# to number of items).
# Problem: collisions! Solution: chaining! Basically, store items for the same hash
# as a linked list

# Simple uniform hashing: each key is equally likely to be hashed to any slot, independent of where
# other keys hashing (i.e. it guarantees randomness)

# Analysis: expected length of chain for n keys and m slots is: (n / m) and this is called alpha (greek letter)
# and is referred to as "load factor" (i.e. how loaded or bloated your table is). Basically, the smaller
# the load factor the bigger the "m" has to be and the faster the search is. Ideally, if m is O(n) (i.e. if
# m is the same as the number of unique keys), then the search is O(1) (i.e. it's constant).
# In worst case, if you have duplicates, for each search you pay O(1 + |chain|) (1 for converting key to integer
# and length of chain for finding the appropriate key in the list). This is actually the same as O(1 + alpha).

# How to construct hash function actually?
# First method --> division method. h(k) = k mod m (gives you a number between 0 and m, and you are done!)
#   in practice - this can be good if m is PRIME and is not factor of 2 or factor of 10 (because pairs of 2s and 10s are very common)
#
# Second method --> multiplication method! h(k) = [ (a * k) mod 2 ^ w ] >> ( w - r )
#   w --> word size in BITs (i.e. how many bits you can handle at once!)
#   a --> connstant integer having "w" bits
#   m is of the size 2 ^ r
#
# Third method (cool method!) is called --> universal hashing!
#   h(k) = [ ( a * k + b) mod p ] mod m
#       a and b are random numbers between 0 and (p - 1)
#       p --> big prime number

def prehash(key):
    """
    Converts anything (string, object, ...) to integer

    In theory, technically speaking, anything on a computer is string of bits,
    and as such already IS a number.

    However, in practice, we need to use something more realistic.

    Python has a hash(x) function that does PREHASHING (it's not HASHING but PREHASHING!)
    """

    return hash(key)

def simple_hash(key, m):
    """

    :param key:
    :param m:
    :return: int
    :rtype: int
    """
    """Does a simple hashing variant -- runs a prehash and then does a mod m over the key"""

    pre_hash = prehash(key)

    return pre_hash % m


class DictionaryValue:
    def __init__(self, key, value, next_element = None):
        self.key = key
        self.value = value
        self.next_element = next_element

class Dictionary:
    def __init__(self, m):
        self.m = m
        self._values = [None for i in range(m)]

    def set_key(self, key, value):
        index = simple_hash(key, self.m)

        if not self._values[index]:
            self._values[index] = DictionaryValue(key, value)
        else:
            current_val = self._values[index]

            self._values[index] = DictionaryValue(key, value, current_val)

    def get_key(self, key):
        index = simple_hash(key, self.m)

        if self._values[index] == None:
            return None
        else:
            el = self._values[index]

            while True:
                if el.key == key:
                    return el.value

                if el.next_element is None:
                    return None

                el = el.next_element



keys = ["kurac", "fakat", "333", "mali tuki", "palac"]

d = Dictionary(m = 3)

# d.set_key("kurac", 555)

for key in keys:
    d.set_key(key, key)
    # print("Key: {}, Hash: {}".format(key, simple_hash(key)))

for key in keys:
    print("Key: {}, Value: {}".format(key, d.get_key(key)))

# print(hash('\0B'))
# print(hash("\0\0C"))