def bucketsort(array):
    max_val = max(array)
    min_val = min(array)
    bucket_count = len(array)
    bucket_size = (max_val - min_val) // bucket_count + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in array:
        buckets[(num - min_val) // bucket_size].append(num)

    sorted_array = []
    for bucket in buckets:
        sorted_array += sorted(bucket)

    return sorted_array

if __name__ == "__main__":
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    sorted_array = bucketsort(array)
    print("Sorted array is:")
    print(sorted_array)