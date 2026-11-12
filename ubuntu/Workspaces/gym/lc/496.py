from typing import List

class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash = {element : -1 for element in nums2}
        monotonic_stack = []

        for element in nums2:

            while len(monotonic_stack) > 0 and monotonic_stack[-1] < element:
                hash[monotonic_stack.pop()] = element

            monotonic_stack.append(element)
        
        return [hash[x] for x in nums1]

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))