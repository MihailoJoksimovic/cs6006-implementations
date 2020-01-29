# Is unique: Implement an algo to determine if a string has all unique chars. What if you can't use additional data structs?

def has_all_unique(string):
    occurences = {}

    if len(string) > 128:
        # We cant have a string that has more than # of ASCII chars and remain unique, lol
        return False

    for letter in string:
        if letter.lower() in occurences:
            return False

        occurences[letter.lower()] = True

    return True

def has_all_unique_2(string):
    """Implementation without using additional data structures"""
    for i in range(0, len(string)):
        key = string[i].lower()

        for j in range(i + 1, len(string)):
            if key == string[j].lower():
                return False

    return True


print(has_all_unique_2("Mixa "))