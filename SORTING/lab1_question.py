import time
import random


#bubble
def bubbleSort(array):
    s=time.process_time()
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
    e=time.process_time()
    print("Bubble Sort: ",e-s,"seconds")


#Selecetion sort
def selectionSort(array):
    a=time.process_time()
    n = len(array)
    for i in range(n):
        #print("Iteration {}:".format(i + 1), array)
        min_idx = i
        for j in range(i + 1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    b=time.process_time()
    print("selection sort:",b-a,"Seconds")


#merger sort
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(L, R, array)
    

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
 

#heapsort

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
        heapify(array, i, 0)      

#using default array.sort(); function to compare the performance of different sorting algorithms
def arr(array):
    x=time.process_time()
    array.sort() 
    z=time.process_time()
    print("Array sort: ",z-x,"Seconds")

if __name__ == "__main__":
    #array = input("Enter the array elements separated by space: ")
    #array = [int(x) for x in array.split()]
    array = [random.randint(1, 1000) for _ in range(10000)]
    selectionSort(array)
    bubbleSort(array)
    mergeSort(array)
    arr(array)
    #heapsort(array)
    print("Sorted array is:")
    print(array)