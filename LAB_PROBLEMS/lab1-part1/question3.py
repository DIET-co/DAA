#Write a recursive function to convert the entered string of digits into the integer it represents.
#For example, 13531 represents the integer 13,531.

def string_to_integer(s):
    if len(s) == 1:
        return int(s)
    else:
        return int(s[0]) * 10 ** (len(s) - 1) + string_to_integer(s[1:])

# Test the function
input_string = input("Enter a string of digits: ")
result = string_to_integer(input_string)
print("The integer representation of '{}' is: {}".format(input_string, result))
