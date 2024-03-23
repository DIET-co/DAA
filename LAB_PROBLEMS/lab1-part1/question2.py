#Perform linear and binary searches for an array of 10000 elements. Use random function in
#Python to generate the integer array elements in the range 1 to 1000. The search key is an input
#given by the user. Plot the time taken by the algorithm for 5 different searches when executing
#the two algorithms.

import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Generate random array of 10,000 elements
arr = [random.randint(1, 1000) for _ in range(10000)]

# Perform searches and plot time taken
search_queries = [random.randint(1, 1000) for _ in range(5)]
linear_times = []
binary_times = []

for query in search_queries:
    start_time = time.time()
    linear_search(arr, query)
    linear_times.append(time.time() - start_time)

    start_time = time.time()
    arr.sort()
    binary_search(arr, query)
    binary_times.append(time.time() - start_time)

# Plotting
plt.plot(search_queries, linear_times, label='Linear Search')
plt.plot(search_queries, binary_times, label='Binary Search')
plt.xlabel('Search Query')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken for Linear and Binary Searches')
plt.legend()
plt.show()
