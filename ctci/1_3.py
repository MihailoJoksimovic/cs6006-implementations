# 1.3 Given a string, replace all whitespaces with %20. You should assume that on the input you are given the length of the string

def replace_whitespaces(string, string_length):
    string_list = list(string)

    j = len(string) - 1

    for i in range(string_length - 1, -1, -1):
        letter = string[i]

        if letter == " ":
            string_list[(j-2):j+1] = "%20"

            j -= 3


        else:
            string_list[j] = letter

            j-= 1

    return "".join(string_list)


string = "Mr John Smith      "

print(replace_whitespaces(string, 13))


# string[2] = "Mix"
