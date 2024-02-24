def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        print("Heapify: ", array)
        heapify(array, n, largest)

def heapsort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        print("Iteration {}: ".format(n - i), array)
        heapify(array, i, 0)

if __name__ == "__main__":
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    heapsort(array)
    print("Sorted array is:")
    print(array)