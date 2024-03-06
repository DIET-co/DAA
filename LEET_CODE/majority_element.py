class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        current = nums[0]
        count = 0
        
        for ele in nums:
            if count == 0:
                current = ele
                count = 1
            elif ele == current:
                count += 1
            else:
                count -= 1
        
        return current
    
solution = Solution()

# Test case 1:
nums = [3,2,3]
majority_element = solution.majorityElement(nums)
print(f"Majority element in test case 1: {majority_element}") # Expected output: 3

# Test case 2:
nums = [2,2,1,1,1,2,2]
majority_element = solution.majorityElement(nums)
print(f"Majority element in test case 2: {majority_element}") # Expected output: 2

# Test case 3:
nums = [1]
majority_element = solution.majorityElement(nums)
print(f"Majority element in test case 3: {majority_element}") # Expected output: 1

# Test case 4:
nums = [1,1,1,2,2,2,2]
majority_element = solution.majorityElement(nums)
print(f"Majority element in test case 4: {majority_element}") # Expected output: 2

# Test case 5:
nums = [1,2,3,4,5,6,7,8,9,10]
majority_element = solution.majorityElement(nums)
print(f"Majority element in test case 5: {majority_element}") 
# Expected output: None (since there is no majority element)    