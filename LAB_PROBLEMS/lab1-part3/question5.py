#Write a program to implement inversion count.
#Given the Input (non-negative integers): A = {10 , 1 , 2 , 4 , 13 , 9 , 5 }
#he number of inversions that are possible are as follows:
#{ ( 10 , 1 ) , ( 10 , 2 ) , ( 10 , 4 ) , ( 10 , 9 ) , ( 10 , 5 ) , ( 13 , 9 ) , ( 13 , 5 ) , ( 9 , 5 ) }
#Total count of inversions are: 8

def merge(arr, temp_arr, left, mid, right):
    inv_count = 0
    i = left  # Index for the left subarray
    j = mid + 1  # Index for the right subarray
    k = left  # Index for the merged subarray

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # If element at left pointer is greater, then it's an inversion
            temp_arr[k] = arr[j]
            j += 1
            inv_count += (mid - i + 1)
        k += 1

    # Copy the remaining elements of left subarray
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the merged elements back to the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        # Recursively count inversions in left and right subarrays
        inv_count += merge_sort(arr, temp_arr, left, mid)
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)

        # Merge the sorted subarrays and count inversions
        inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count

def inversion_count(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_sort(arr, temp_arr, 0, n - 1)

# Example usage:
A = [10, 1, 2, 4, 13, 9, 5]
print("Number of inversions:", inversion_count(A))
