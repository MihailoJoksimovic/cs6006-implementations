# Binary to String: Given a real number between 0 and 1 (e.g. 0.72), that is passed as double, print the binary repr.
# If the nuber has more than 32 chars -- print ERROR

num = 0.72

string = "0."

while num > 0:
    r = num * 2

    if r >= 1:
        string += "1"
        num = r - 1
    else:
        string += "0"
        num = r

print(string)

import unittest


def bin_to_string(num):
    result = []
    while num and len(result) <= 32:
        num *= 2
        if num >= 1:
            result.append('1')
            num -= 1
        else:
            result.append('0')

    if len(result) > 32:
        raise ValueError('Binary cannot be represented with 32 bits')

    return '.' + ''.join(result)


class Test(unittest.TestCase):

    def test_bin_to_string(self):
        self.assertEqual(bin_to_string(.5), '.1')
        self.assertEqual(bin_to_string(.25), '.01')
        self.assertEqual(bin_to_string(.125), '.001')
        self.assertEqual(bin_to_string(.625), '.101')
        # self.assertEqual(bin_to_string(.63), '.101')
        self.assertRaises(ValueError, bin_to_string, .1)


# if __name__ == '__main__':
#     unittest.main()

bin_to_string(.625)
