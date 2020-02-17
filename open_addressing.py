# If there is ONE thing that you will remember from Hashing lectures, it should be OPEN ADDRESSING. It's, apparently,
# the simplest way to implement hashing
# Open addressing --> implementing the hash table using a simple array, without linked lists, chaining, etc.
#   The problem is collisions - if you had no collisions, simple array would do.
#   We dont want to use chaining!
#   We are assuming that ONE ITEM goes to one slot (one index)! We dont want chaining!
#       This also means that m >= n     (m -- # of slots in table, n -- # of elements)
#   How to do this? PROBING! So the idea is you try to calculate key, and if the calculated slot is NOT EMPTY, you do
#       a slightly different recalculation. And you repeat this until you find a free slot.
#   We need a hash function where we can specify order of slots to probe for a key (and this is true for insert/search/delete)
#   Hash function needs to take two arguments --> requested key AND the trial count.
#   You also want to assume that each probe has equal chance of putting a key to an empty slot, as you dont want to end
#       up buffering bunch of slots in one part of the table. So we really want to have this uniformly arranged.
#   So, in a NUTSHELL, INSERT works by probing the keys until it finds empty slot. SEARCH works almost the same, probes
#       the slots until it either encounters the requested KEY, or finds NONE.
#   Now, DELETE has a problem, because if you delete a key in the MIDDLE of the sequence, then, when SEARCHING, you have
#       to know that you have to keep trying, obviously. So we need a FLAG to indicate a DELETED element. In the lecture,
#       they use the DeleteMe flag, which indicates a deletion. Hence, Search and insert need to be updated to take this
#       into account
# So how do you approach the "probing"? Well, one approach is to just calculate the hash() and if it's occupied, do a
#   hash() + 1, hash() + 2, etc. This WILL do the work, but the problem is that it will create CLUSTERS (i.e. the keys
#   will start clustering). This approach is also called LINEAR PROBING.
# Alternative approach is called DOUBLE hashing. The idea is that you basically calculate two hashes and then do a mod m:
#   h(k, i) = (h1(k) + i * h2(k)) mod m
#
# Uniform Hashing Assumption -- each key is equally likely to have any of the m! permutations as its probe sequence!
#
# In general, when implementing the Open Addressing, you want to make sure that you keep alpha (n / m ==> load factor)
# fairly low, because if not, you will end up with bunch of probes each time you insert. So, keep alpha low and grow
# the table as soon as alpha gets over 0.5

class DeleteMe:
    pass

class OpenAddressingHashtable:
    def __init__(self, m = 8):
        self.__m = m
        self.__values = [(None, None)] * self.__m

    def insert(self, key, value, order = 1):
        if order > self.__m:
            raise ValueError("Order parameter exceeds size of array")

        # Calculate the index for given order. If the slot for given index is not empty --> try increasing order
        index = self.__calculate_index(key, order)

        if self.__values[index][0] is None or isinstance(self.__values[index][0], DeleteMe):
            # Found empty slot - we're done
            self.__values[index] = (key, value)

            return index

        if self.__values[index][0] is not None:
            return self.insert(key, order + 1)

        # For sake of fun, return index where we inserted the key :)
        return index

    def search(self, key, order = 1):
        if order > self.__m:
            # We searched the whole table ... no point any more :)
            return None

        # Calculate the index for given order. If the slot given does NOT match the key and IS not None - try again
        # If it matches the key -- return it

        index = self.__calculate_index(key, order)

        slot_element = self.__values[index]

        if slot_element[0] is None:
            return None

        if slot_element[0] != key:
            # keep probing padawan!
            return self.search(index, order + 1)

        return self.__values[index][1]


    def __calculate_index(self, key, order):
        pass

