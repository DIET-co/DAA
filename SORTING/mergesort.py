def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(L, R, array)
        print("Recursive call: ", array)

def merge(L, R, array):
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

if __name__ == "__main__":
    array = [34, 3, 89, 20, 47, 2, 65]
    #array = input("Enter the array elements separated by space: ")
    #array = [int(x) for x in array.split()]
    mergeSort(array)
    print("Sorted array is:")
    print(array)