from typing import List

class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        S = n * (n + 1) // 2

        for num in nums:
            S -= num

        return S

nums = [9, 6, 4 , 2, 3, 5, 7, 0, 1]
nums = [0, 1]
print(Solution().missingNumber(nums))
