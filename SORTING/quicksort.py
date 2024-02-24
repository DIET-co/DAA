def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        print("Recursive call: ", array)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

if __name__ == "__main__":
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    quicksort(array, 0, len(array) - 1)
    print("Sorted array is:")
    print(array)