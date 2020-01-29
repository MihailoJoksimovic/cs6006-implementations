# Given a string, check if string is a permutation of a palindrome

# From what I see, for a String to be a palindrome, it has to:
#   1. Has odd number of characters (penis --> this is not true because of Space ...)
#   2. Has to have same number of all chars., EXCEPT one!

def is_palindrome_permutation(string):
    # if (len(string) % 2) == 0:
    #     # has to be odd number of characters
    #     return False

    letters = {}

    for letter in string:
        if letter == " ":
            continue

        if letter not in letters:
            letters[letter.lower()] = 1
        else:
            letters[letter.lower()] += 1

    max_num_of_chars = None
    found_one_letter_char = False

    for letter in letters.keys():
        occurences = letters[letter]

        if occurences == 1:
            if found_one_letter_char:
                # if there was already another one-letter char then we're not palindrome
                return False

            found_one_letter_char = True

            continue

        if max_num_of_chars is None:
            max_num_of_chars = occurences

            continue

        if max_num_of_chars != occurences:
            # Found a different number of chars --> not a palindrome ;)
            return False

    return True

        # print("{}: #{}".format(letter, letters[letter]))

print(is_palindrome_permutation("Tact coa2"))
