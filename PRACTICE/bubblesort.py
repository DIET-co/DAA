def bubblesort(array):
    n = len(array)
    for i in range(n):
         for j in range(0,n-i-1):
             if array[j] > array[j+1]:
                 array[j],array[j+1]=array[j+1],array[j]
                

if __name__ == "__main__":
    array = input("Enter array elements with space:")
    array = [int(x) for x in array.split()]
    bubblesort(array)
    print ("Sorted array is:", end=" ")
    print (array)
                  
