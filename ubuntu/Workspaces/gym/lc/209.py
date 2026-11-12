from typing import List

class Solution:

    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
    #     result = float("inf")

    #     i, sum = 0, 0
    #     for j in range(len(nums)):
            
    #         sum += nums[j]

    #         if sum > target:

    #             while sum > target:
    #                 sum -= nums[i]
    #                 i += 1
                
    #             result = min(result, j - i + 2)
            
    #         if sum == target:
    #             result = min(result, j - i + 1)

    #     return result if result != float("inf") else 0
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        result = float("inf")

        i, sum = 0, 0
        for j in range(len(nums)):
            
            sum += nums[j]

            while sum >= target:
                result = min(result, j - i + 1)
                sum -= nums[i]
                i += 1
                            
        return result if result != float("inf") else 0

# target, nums = 7, [2, 3, 1, 2, 4, 3]
# target, nums = 11, [1, 1, 1, 1, 1, 1, 1, 1]
# target, nums = 213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
# target, nums = 11, [1, 2, 3, 4, 5]
target, nums = 5, [2, 3, 1, 1, 1, 1, 1]
print(Solution().minSubArrayLen(target, nums))