from typing import List

class Solution:
    
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        lb, ub = 0, len(nums) - 1

        while lb < ub:
            
            m = lb + (ub - lb) // 2
                    
            if nums[m] > nums[lb]:
                lb = m
            else:
                ub = m
        
        return nums[m + 1]

nums = [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
nums = [3, 4, 5, 1, 2]
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1]
print(Solution().findMin(nums))
