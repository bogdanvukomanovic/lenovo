from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        accumulator = nums[0]
        for num in nums[1:]:
            accumulator = accumulator ^ num

        return accumulator

nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums))
