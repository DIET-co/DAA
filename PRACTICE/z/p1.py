def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(L, R, array)
        print("Recursive Call:", array)

def merge(L,  R, array):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        print("Iteration {}:".format(i + 1), array)
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        print("Recursive Call:",array)
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
    array =  [38, 27, 43, 31, 5,  46, 20, 49, 44, 19, 2, 80]
    array_2 =  [38, 27, 43, 31, 5,  46, 20, 49, 44, 19, 2, 80]
    array_3 =  [38, 27, 43, 31, 5,  46, 20, 49, 44, 19, 2, 80]
    print('--'*40)
    mergeSort(array)
    print("sorted array is:",array)
    print("--"*40)
    bubbleSort(array_2)
    print("Bubble sorted array is: ", array_2)
    print("--"*40)
    quicksort(array_3, 0, len(array_3) - 1)
    print("Quick sorted array is :", array_3)
    print("--"*40)
    