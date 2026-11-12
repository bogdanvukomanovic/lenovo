from typing import List

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        DP = [num for num in nums]
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                DP[i] = max(DP[i], nums[i] + DP[j]) 

        return max(DP)

nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))