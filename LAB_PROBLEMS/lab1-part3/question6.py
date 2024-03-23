#An array contains N numbers, and you want to determine whether two of the numbers sum
#to a given number K. For example, if the input is 8, 4, 1, 6 and K is 10, the answer is yes
#(4 and 6). A number may be used twice.
#a. Give an 𝑂(𝑛
#2
#) algorithm to solve this problem.
#b. Give an 𝑂(𝑛𝑙𝑜𝑔𝑛) algorithm to solve this problem.
#(Hint: first sort the array and then solve the problem in linear time).


def has_pair_with_sum_nlogn(arr, K):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == K:
            return True
        elif arr[left] + arr[right] < K:
            left += 1
        else:
            right -= 1
    return False

# Example usage:
arr = [8, 4, 1, 6]
K = 10
print(has_pair_with_sum_nlogn(arr, K))  # Output: True (4 and 6)
