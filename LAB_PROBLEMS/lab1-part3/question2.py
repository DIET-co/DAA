#Given an unsorted integer array containing both positive and negative numbers, find a
#pair with maximum product in it.
#Input:
#If we have an array say arr = [1, 7, 4, 2, 8, 6, 3, 9, 5]
#Then in this array first two bigger numbers are 9 and 8.
#So, product is 9*8=72 which is maximum product

def max_product_pair(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a pair

    max1 = max2 = float('-inf')  # Initialize maximum and second maximum

    min1 = min2 = float('inf')  # Initialize minimum and second minimum

    # Iterate through the array
    for num in arr:
        # Update maximum and second maximum
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        # Update minimum and second minimum
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # Return the pair with maximum product
    if max1 * max2 > min1 * min2:
        return (max1, max2)
    else:
        return (min1, min2)

# Example usage:
arr = [1, 7, 4, 2, 8, 6, 3, 9, 5]
pair = max_product_pair(arr)
if pair:
    print("Pair with maximum product:", pair, "Product:", pair[0] * pair[1])
else:
    print("No pair found in the array.")
