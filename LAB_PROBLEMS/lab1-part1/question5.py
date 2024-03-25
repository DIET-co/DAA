#Write a short recursive Python function that determines if a string s is a palindrome. For
#example, racecar and gohangasalamiimalasagnahog are palindromes.

def is_palindrome(s):
    # Base case: if the string has zero or one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Check if the first and last characters are the same
    if s[0] != s[-1]:
        return False
    # Recursive step: check if the substring excluding the first and last characters is a palindrome
    return is_palindrome(s[1:-1])


strings = ["racecar", "gohangasalamiimalasagnahog", "hello", "level", "radar"]
for string in strings:
    print(f"{string}: {is_palindrome(string)}")
