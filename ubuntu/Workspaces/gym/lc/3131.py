from typing import List

class Solution:

    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)

print(Solution().addedInteger([2, 6, 4], [9, 7, 5]))
