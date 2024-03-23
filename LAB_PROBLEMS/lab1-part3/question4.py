#Given a binary array of 0’s and 1’s. Segregate all 0’s followed by 1.
##

def segregate_zeros_and_ones(arr):
    left = 0  # Left pointer
    right = len(arr) - 1  # Right pointer

    while left < right:
        # Move left pointer until it points to a 1
        while arr[left] == 0 and left < right:
            left += 1

        # Move right pointer until it points to a 0
        while arr[right] == 1 and left < right:
            right -= 1

        # Swap 0 at left pointer with 1 at right pointer
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

# Example usage:
binary_array = [0, 1, 0, 1, 1, 0, 0, 1]
segregated_array = segregate_zeros_and_ones(binary_array)
print("Segregated array:", segregated_array)
