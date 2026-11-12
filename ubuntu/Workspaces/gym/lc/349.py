from typing import List


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [n1 for n1 in set(nums1) if n1 in set(nums2)]


nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
print(Solution().intersection(nums1, nums2))
