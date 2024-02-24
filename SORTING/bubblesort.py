def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == "__main__":
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    bubbleSort(array)
    print("Sorted array is:")
    print(array)

'''def bubbleSort(array):
    n = len(array)
    for i in range(n):
        print("Iteration {}:".format(i + 1), array)
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == "__main__":
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    bubbleSort(array)
    print("Sorted array is:")
    print(array)'''

