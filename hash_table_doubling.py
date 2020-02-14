# How to pick m? You pick a random number that is multiple of 2, and then you grow and shrink as necessary

# When n outgrows m, we want to grow the table. What needs to be done to grow a table? First you allocate new memory,
# and then you recalculate the hashes for new m.
# Question: how much do you grow the table actually? You always DOUBLE it
#
# Ammortization -- the idea that, even though you have to grow all the time, at some point you stop growing so much
# so the ammortized time is actually constant. For example, if you start with m = 8, then you grow to m = 16, then 32,
# 64, etc. At some point, it takes way more keys to actually grow. So, you can assume that your ammortized time is
# constant ...
#
# There's also a concept of SHRINKING the table. Basically, if we delete the keys, we should care about SHRINKING as well.
# When to shrink? If we shrink every time that m = n / 2, that is theoretically OK, but the problem is if m is 8, and
# we insert 9th item, and we grow to 16, but then we delete one item and we shrink back to 8 ... So we'll be ping ponging
# back and forth and that's no good! The good strategy is anything above m / 2, for example m / 4. So every time you
# reduce keys to m / 4, you shrink to m / 2, but when growing, you always go 2 * m. This ensures that when you shrink,
# you trigger shrinking on quarters only, but you still have to grow m / 2 to trigger the growth again.
# One final note is that Python lists are implemented sa ARRAYS and use table doubling. Hence, the pop() and append()
# have ammortized O(1) time which is cool actually. Since they are arrays, pop() just removes the LAST ELEMENT of array,
# while append() is generally ammortized due to table doubling.
#
# There is one interesting technique used in real-time systems that allows WORST-CASE time to be O(1). This is achieved
# by starting to grow a NEW double-sized table when you "see" that your current table is going to become full. So, once
# you realize you are going to be full, you start a new table on the side and slowly copy the elements over there, so
# that by the time you reach the end of your current list, you just switch to a new one. Basically yeah, space complexity
# is way bigger but I guess it's OK to afford that ...
#
# So, string matching ... We want to see if substring "s" occurs in some huge string "t". One obvious way is to check
# substring one by one until we find a match, and that's basically linear time ...
#
# Solution: rolling-hashes! How you prehash? You prehash by storing the string as a number of modulo of the alphabet
# that you are using. And you calculate rolling hashes by the formula that he gave basically .. phew ... have to check
# the notes really

class Dictionary:
    def __init__(self):
        # Let's start with initial size being 8
        self._m = 2

        # Num. of elements in use
        self._num_used_elements = 0

        # Initialize the initial array
        self._elements = [(None, None)] * self._m

    def set(self, key, value):
        index = self.__get_index(key)

        if self._elements[index][0] is None:
            self._num_used_elements += 1

        self._elements[index] = (key, value)

        if (self._m - 1) == self._num_used_elements:
            self.__grow()

        pass

    def get(self, key):
        index = self.__get_index(key)

        if self._elements[index]:
            return self._elements[index][0]

        return None

    def __get_index(self, key):
        return (self.__prehash(key) % self._m)

    def __prehash(self, key):
        """Calculate pre-hash of the given key (i.e. convert it to integer, really)"""
        return hash(key)

    def __grow(self):
        # So we grow by doubling in the size ...
        new_elements = [(None, None)] * (self._m * 2)

        self._m = self._m * 2

        # Recalculate all previously set keys
        for element in self._elements:
            key = element[0]
            val = element[1]

            if key is None:
                continue

            new_index = self.__get_index(key)

            new_elements[new_index] = (key, val)

        self._elements = new_elements

    def __shrink(self):
        pass

d = Dictionary()


keys = ["Kurac", "palac", "kriminalac", "jadac", "cmarac", "palac", "falac", "kriminalac"]

for key in keys:
    d.set(key, key)

for key in keys:
    print(d.get(key))