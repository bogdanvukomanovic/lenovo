from typing import List

class Solution:

    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
           
            result = max(result, (r - l) * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1

        return result

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
heights = [1, 1]
print(Solution().maxArea(heights))