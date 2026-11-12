from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        lb, ub = 0, len(nums) - 1

        while lb < ub:
            
            m = lb + (ub - lb) // 2
            
            if target <= nums[m]:
                ub = m
            else:
                lb = m + 1

        return lb if nums[lb] == target else -1


nums, target = [-1, 0, 3, 5, 9, 12], 9
nums, target = [-1, 0, 3, 5, 9, 12], 2
nums, target = [1], 1

print(Solution().search(nums, target))