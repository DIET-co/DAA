def get_max_digits(array):
    max_val = max(array)
    digits = 0
    while max_val > 0:
        max_val //= 10
        digits += 1
    return digits

def radixsort(array):
    max_digits = get_max_digits(array)
    buckets = [[] for _ in range(10)]

    for k in range(max_digits):
        for num in array:
            digit = (num // (10 ** k)) % 10
            buckets[digit].append(num)

        array.clear()
        for bucket in buckets:
            array += bucket
            buckets = [[] for _ in range(10)]

if __name__ == "__main__":
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    radixsort(array)
    print("Sorted array is:")
    print(array)