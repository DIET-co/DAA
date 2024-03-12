class Solution:
    def countTriplet(self, arr, n):
        count = 0
        hash_table = {}

        for i in range(n):
            hash_table[arr[i]] = hash_table.get(arr[i], 0) + 1

        for i in range(n):
            for j in range(i):
                target = n - arr[i] - arr[j]
                if target in hash_table:
                    count += hash

arr = [1, 2, 3, 4, 5]
n = len(arr)

solution = Solution()
result = solution.countTriplet(arr, n)

print(result)                    