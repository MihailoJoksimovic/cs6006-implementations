# Next Number: Given a positive integer, print the next smallest and the next largest number that have the same number
# of 1 bits in their binary representation.

# Algorithm:

# Smaller number is found by finding rightmost 10 combination and flipping the bits. If there is no rightmost 10,
# then there is no smaller number.

# Next largest number is found by looking for rightmost "01" and flipping to "10". If there is no such sequence, see if
# the least significant bit is 0. If it's 0, then we shift all but last to the end, we append two zeros and then add one
# more bit to be 1.
# If the least significant bit is 1, then we set last bit to 0 and append 1 as most significant bit.

number = 0b11

def get_bit(number, position):
    return 1 if (number & (1 << position)) != 0 else 0

def update_bit(number, position, new_val):
    # First set the bit to 0, then set to desired val
    mask = ~ (1 << position)

    # First set bit in the desired position to 0, then we will update it to 1
    number = number & mask

    if (new_val == 1):
        number |= 1 << position

    return number

def get_10_mask(position):
    if position == 0:
        return (~ 0) << 1

    mask = 1024 # All ones

    mask = mask ^ (1 << position)

    return mask

def get_msb_position(number):
    # We'll only go up to 32 bits ...

    i = 31

    while i >= 0:
        if get_bit(number, i) == 1:
            return i

        i -= 1

    return -1


def get_next_smaller(number):
    for i in range(30):

        if get_bit(number, i + 1) == 1 and get_bit(number, i) == 0:
            new_number = update_bit(number, i + 1, 0)
            new_number = update_bit(new_number, i, 1)

            return new_number

    return 0

def get_next_largest(number):
    msb_position = get_msb_position(number)

    for i in range(msb_position):
        if get_bit(number, i + 1) == 0 and get_bit(number, i) == 1:
            new_number = update_bit(number, i + 1, 1)
            new_number = update_bit(new_number, i, 0)

            return new_number

    # No "01" combination, then do the alternative dance --

    # Is the LSB == 1? If so, this is sort of easy --> just replace MSB with 0 and append 1.
    if (number & 0b1) == 1:
        msb_position = get_msb_position(number)

        mask = ~ (1 << msb_position)

        new_number = number & mask

        new_number = new_number | (1 << msb_position + 1)

        return new_number

    else:
        new_number = number >> 1
        new_number = update_bit(new_number, msb_position - 1, 0)
        new_number = update_bit(new_number, msb_position, 0)
        new_number = update_bit(new_number, msb_position + 1, 1)

        return  new_number

    # Is the last bit 0? If so, then do the following --> shift all to right by 1, append two zeros and set 1.

    return 0


number2 = 0b001010

# print("Original: {} ({})".format(number, bin(number)))
# print("Next:     {} ({})".format(get_next_smaller(number), bin(get_next_smaller(number))))

# for i in range(10):
#     print(bin(get_10_mask(i)))

# print(get_bit(0b01, 0))

# print(get_msb_position(0b1001010))

number = 0b11110

print("Original: {} ({})".format(number, bin(number)))
print("Larger:   {} ({})".format(get_next_largest(number), bin(get_next_largest(number))))

# print(bin(get_next_largest(0b11111)))