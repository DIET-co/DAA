#Find the sum of first N natural numbers using Iterative and Recursive algorithms. Find the time
#taken to execute the same by varying ‘N’s value and plot it using python’s plot function

import time
import matplotlib.pyplot as plt

# Iterative algorithm to find the sum of first N natural numbers
def sum_iterative(N):
    result = 0
    for i in range(1, N + 1):
        result += i
    return result

# Recursive algorithm to find the sum of first N natural numbers
def sum_recursive(N):
    if N == 0:
        return 0
    return N + sum_recursive(N - 1)

# Function to measure execution time for a given function and value of N
def measure_time(func, N):
    start_time = time.time()
    func(N)
    end_time = time.time()
    return end_time - start_time

# Varying values of N
N_values = list(range(1, 1000, 100))  # You can adjust the range as needed

# Measure time for both algorithms for each value of N
iterative_times = []
recursive_times = []
for N in N_values:
    iterative_times.append(measure_time(sum_iterative, N))
    recursive_times.append(measure_time(sum_recursive, N))

# Plotting
plt.plot(N_values, iterative_times, label='Iterative')
plt.plot(N_values, recursive_times, label='Recursive')
plt.xlabel('Value of N')
plt.ylabel('Time (seconds)')
plt.title('Time taken for different values of N')
plt.legend()
plt.show()
