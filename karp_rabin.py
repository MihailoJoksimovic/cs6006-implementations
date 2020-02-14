def string_to_int(string):
    """Converts the given string into an integer"""

    total = 0

    for c in string:
        total += ord(c)

    return total % 256

def search(pattern, string):
    """Search for a given pattern in a given string. Should return index where the pattern occurs or None otherwise"""

    pass

class RollingHash:
    def __init__(self):
        self._hash = 0
        self.string = ""

    def append(self, char):
        """Append a char to the end of rolling hash"""

        self.string += char

        self._hash = string_to_int(self.string)

    def skip(self, char):
        """Remove a char from the beginning of rolling hash"""

        self.string = self.string[1:]

        self._hash = string_to_int(self.string)


    def get_hash(self):
        return self._hash


pattern = "Mixa"
sentence = "Kurac Mixa moze da mi sisa kurac"

pattern_rollinghash = RollingHash()

for c in pattern:
    pattern_rollinghash.append(c)

print(pattern_rollinghash.get_hash())

# now let's iterate through the sentence and look for matches
sentence_rollinghash = RollingHash()

for i in range(len(pattern)):
    sentence_rollinghash.append(sentence[i])

if sentence_rollinghash.get_hash() == pattern_rollinghash.get_hash():
    print("Match found on beginning of string!")

    exit()

# Ok, let's iterate and look for ... matches! :)

for i in range(1, (len(sentence) - len(pattern))):
    sentence_rollinghash.skip(sentence[i - 1])
    sentence_rollinghash.append(sentence[i+len(pattern)])

    if sentence_rollinghash.get_hash() == pattern_rollinghash.get_hash():
        print("match found at index {}".format(i))

        break


