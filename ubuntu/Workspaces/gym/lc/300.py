from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        LIS = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):

                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

    '''
        TODO: This problem can also be solved with:
                1) Greedy with Binary Search
                2) Binary Indexed Tree 
                3) Segment Tree
                
              Reference: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/
    '''

nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [7, 7, 7, 7, 7, 7, 7]
nums = [0, 1, 0, 3, 2, 3]
print(Solution().lengthOfLIS(nums))