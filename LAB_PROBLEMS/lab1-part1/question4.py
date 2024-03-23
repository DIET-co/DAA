#Write a short recursive Python function that takes a character string s and outputs its reverse.
#For example, the reverse of pots&pans would be snap&stop.

def reverse_string(s):
    # Base case: if the string is empty or has only one character, return itself
    if len(s) <= 1:
        return s
    else:
        # Recursive step: concatenate the last character of the string with the reversed substring
        return s[-1] + reverse_string(s[:-1])

# Test the function
original_string = "pots&pans"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)
