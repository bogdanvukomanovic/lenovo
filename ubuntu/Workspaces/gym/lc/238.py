from typing import List

class Solution:

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    #     accumulator, zero_count = 1, 0
        
    #     for x in nums:
    #         if x == 0:
    #             zero_count += 1
    #         else:
    #             accumulator *= x
        
    #     for i in range(0, len(nums)):
    #         if nums[i] != 0:
    #             nums[i] = 0 if zero_count else int(accumulator / nums[i])
    #         else:
    #             nums[i] = 0 if zero_count > 1 else accumulator
        
    #     return nums

    
    # You must write an algorithm that runs in O(n) time and without using the division operation.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        LR = [nums[0]] * n
        RL = [nums[n-1]] * n

        for i in range(1, n):
            LR[i] = LR[i-1] * nums[i]
            RL[n-1-i] = RL[n-i] * nums[n-1-i]

        nums[0] = RL[1]
        nums[n-1] = LR[n-2]

        for i in range(1, n - 1):
            nums[i] = LR[i-1] * RL[i+1]

        return nums

nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))