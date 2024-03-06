class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()
        
        for i in range(len(nums)):
            if target - nums[i] in d:
                j = d[target - nums[i]]
                return [i, j]
            else:
                d[nums[i]] = i
        
        return [-1, -1]
    
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]    