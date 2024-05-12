def shift_text(text, shift):
    """Shifts the text by the given number of positions."""
    shifted = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            shifted.append(shifted_char)
        else:
            shifted.append(char)
    return ''.join(shifted)

def encrypt(text, shift):
    """Encrypts the text using a shift cipher and rearranges in reversed groups of three."""
    # Shift the characters
    shifted = shift_text(text, shift)
    # Break into groups of three
    groups = [shifted[i:i+3] for i in range(0, len(shifted), 3)]
    # Reverse the order of groups
    groups.reverse()
    # Join groups back into a string
    return ''.join(groups)

def decrypt(encrypted_text, shift):
    """Decrypts the text by reversing the encryption process."""
    # Reverse the group order processing
    groups = [encrypted_text[i:i+3] for i in range(0, len(encrypted_text), 3)]
    groups.reverse()
    # Join groups and shift back
    joined = ''.join(groups)
    # Shift back to original
    return shift_text(joined, -shift)

# Example usage
original_text = "hello world"
shift_amount = 3
encrypted = encrypt(original_text, shift_amount)
decrypted = decrypt(encrypted, shift_amount)

print("Original:", original_text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
