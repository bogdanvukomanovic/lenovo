from typing import List

class Solution:

    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

nums = [1, 3, 1, 2]
print(Solution().getConcatenation(nums))
