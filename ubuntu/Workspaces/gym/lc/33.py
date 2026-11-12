from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        lb = 0
        ub = len(nums) - 1

        while lb <= ub:

            m = lb + (ub - lb) // 2
  
            if nums[m] == target:
                return m
            
            if nums[lb] <= nums[m]:
                if nums[lb] <= target < nums[m]:
                    ub = m - 1
                else:
                    lb = m + 1
            else:
                if nums[m] < target <= nums[ub]:
                    lb = m + 1
                else:
                    ub = m - 1

        return -1

nums, target = [4, 5, 6, 7, 0, 1, 2], 4
nums, target = [0, 1, 2, 3, 4, 5, 6, 7], 8
# nums, target = [4, 5, 6, 7, 0, 1, 2], 3
# nums, target = [1], 1
nums, target = [3, 1], 1
print(Solution().search(nums, target))