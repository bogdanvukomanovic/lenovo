from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}
        for i, n in enumerate(nums):
            
            if target - n in hash:
                return [hash[target - n], i]
            else:
                hash[n] = i

nums, target = [2,7,11,15], 9
nums, target = [3,2,4], 6
nums, target = [3,3], 6
print(Solution().twoSum(nums, target))