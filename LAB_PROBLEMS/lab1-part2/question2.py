#Given ‘m’ sorted lists/ arrays, each containing ‘n’ elements, print them efficiently in sorted
#order

def print_sorted_arrays(arrays):
    # Merge all arrays into a single list
    merged = []
    for arr in arrays:
        merged.extend(arr)

    # Bubble sort to sort the merged list
    n = len(merged)
    for i in range(n):
        for j in range(0, n-i-1):
            if merged[j] > merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]

    # Print the sorted elements
    for num in merged:
        print(num, end=' ')

# Example usage
m = 3  # Number of unsorted arrays
n = 4  # Number of elements in each array

# Generating example unsorted arrays
unsorted_arrays = []
for i in range(m):
    unsorted_arrays.append([i * n + j for j in range(1, n + 1)])

# Printing the unsorted arrays
print("Unsorted Arrays:")
for arr in unsorted_arrays:
    print(arr)

# Printing the arrays in sorted order
print("\nArrays in Sorted Order:")
print_sorted_arrays(unsorted_arrays)
