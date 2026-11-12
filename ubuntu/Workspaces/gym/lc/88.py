from typing import List

class Solution:
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m - 1
        j = n - 1
        write = m + n - 1
        
        while j >= 0:

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1

            write -= 1

        return nums1

nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
# nums1 = [1]; m = 1; nums2 = []; n = 0
# nums1 = [0]; m = 0; nums2 = [1]; n = 1
# nums1 = [0,0,3,0,0,0,0,0,0]; m = 3; nums2 = [1,1,1,2,17,55]; n = 6
# nums1 = [2,0]; m = 1; nums2 = [1]; n = 1
nums1 = [4,5,6,0,0,0]; m = 3; nums2 = [1,2,3]; n = 3 



print(Solution().merge(nums1, m, nums2, n))