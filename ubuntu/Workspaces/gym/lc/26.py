from typing import List

class Solution:
    
    # def removeDuplicates(self, nums: List[int]) -> int:

    #     n = len(nums)
    #     i, j = 0, 0

    #     if nums[-1] == nums[0]:
    #         return 1

    #     while j < n - 1 and nums[0] == nums[j]:
    #         j += 1
    
    #     while i < n - 1 and i < j:

    #         if nums[i] >= nums[i+1]:
    #             nums[i+1] = nums[j]

    #         x = nums[j]
    #         while j < n and x == nums[j]:
    #             j += 1
            
    #         i += 1
            
    #         if nums[i] == nums[-1]:
    #             break          

    #     return i + 1 

    # def removeDuplicates(self, nums: List[int]) -> int:

    #     # Try counting sort because all elements of array nums are -100 <= nums[i] <= 100.
    #     lb, ub = -100, 100 
    #     count = [0] * (ub - lb + 1)

    #     for n in nums:
    #         count[n + ub] += 1
        
    #     k = 0
    #     for i, c in enumerate(count):
    #         if c != 0:
    #             nums[k] = i - ub
    #             k += 1

    #     return k

    def removeDuplicates(self, nums: List[int]) -> int:
        
        i, j = 0, 1

        while i <= j and j < len(nums):
    
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1

        return i + 1

nums = [0,1,1,1,1,2]
print(Solution().removeDuplicates(nums))