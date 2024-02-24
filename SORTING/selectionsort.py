def selectionSort(array):
    n = len(array)
    for i in range(n):
        print("Iteration {}:".format(i + 1), array)
        min_idx = i
        for j in range(i + 1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

if __name__ == "__main__":
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    selectionSort(array)
    print("Sorted array is:")
    print(array)