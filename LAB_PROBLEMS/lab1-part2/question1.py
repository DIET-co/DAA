#1. Generate 1000 integer random numbers between 1 and 10000. Compare the sorting
#algorithms learnt in the class using the same set of numbers generated. Plot the time taken
#for them to complete the process.

import random
import time
import matplotlib.pyplot as plt

# Function to generate random integers
def generate_random_numbers(n):
    return [random.randint(1, 10000) for _ in range(n)]

# Bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion sort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Quick sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge sort algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

# Heap sort algorithm
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Test each sorting algorithm and measure time taken
sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort
}
sorting_times = {algo: [] for algo in sorting_algorithms}

for _ in range(1000):
    numbers = generate_random_numbers(1000)
    for algo_name, algo_func in sorting_algorithms.items():
        start_time = time.time()
        algo_func(numbers.copy())
        end_time = time.time()
        sorting_times[algo_name].append(end_time - start_time)

# Plotting
plt.figure(figsize=(10, 6))
for algo_name, times in sorting_times.items():
    plt.plot(times, label=algo_name)
plt.xlabel("Iteration")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithms Comparison")
plt.legend()
plt.grid(True)
plt.show()
