#Given an array where all its elements are sorted except two swapped elements, sort it in
#linear time. Assume there are no duplicates in the array

def sort_array_with_two_swapped(arr):
    n = len(arr)
    first_swap = second_swap = None

    # Find the two elements that are out of order
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if first_swap is None:
                first_swap = i
            else:
                second_swap = i + 1
                break

    # If second swap index is not found, then the elements are adjacent
    if second_swap is None:
        second_swap = first_swap + 1

    # Swap the elements back to their correct positions
    arr[first_swap], arr[second_swap] = arr[second_swap], arr[first_swap]

    return arr

# Example usage:
arr = [1, 4, 3, 2, 5, 6]
sorted_arr = sort_array_with_two_swapped(arr)
print("Sorted array:", sorted_arr)
