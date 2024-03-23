#Given an array of size N, find the K largest elements in the array where K<<<N
import heapq

def find_k_largest(arr, k):
    # Create a min-heap
    min_heap = []
    
    # Traverse the array
    for num in arr:
        # If heap is not full, push the element
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            # If the current element is larger than the smallest element in the heap
            if num > min_heap[0]:
                # Replace the smallest element with the current element
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
    
    # The min-heap now contains the K largest elements
    return min_heap

# Example usage:
arr = [3, 1, 5, 12, 2, 11]
k = 3
result = find_k_largest(arr, k)
print("The", k, "largest elements are:", result)

class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [None] * (max_size + 1)

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        if self.size == self.max_size:
            if value > self.heap[0]:
                self.heap[0] = value
                self.min_heapify(0)
        else:
            self.heap[self.size] = value
            self.size += 1
            self.heapify_up(self.size - 1)

    def heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def min_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i

        if l < self.size and self.heap[l] < self.heap[i]:
            smallest = l
        if r < self.size and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def get_min(self):
        return self.heap[0]

    def get_heap(self):
        return self.heap


def find_k_largest(arr, k):
    # Create a min-heap of size K
    min_heap = MinHeap(k)

    # Insert first K elements
    for i in range(k):
        min_heap.insert(arr[i])

    # Iterate through the remaining elements
    for i in range(k, len(arr)):
        if arr[i] > min_heap.get_min():
            min_heap.insert(arr[i])

    return min_heap.get_heap()[:k]


# Example usage:
arr = [3, 1, 5, 12, 2, 11]
k = 3
result = find_k_largest(arr, k)
print("The", k, "largest elements are:", result)
