from typing import List

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        
        area = 0

        stack = []
        for i, height in enumerate(heights):
            
            j = i
            while stack and height < stack[-1][1]:
                area = max(area, (i - stack[-1][0]) * stack[-1][1])
                j = stack.pop()[0]

            stack.append((j, height, i))

        for x in stack:
            area = max(area, (stack[-1][2] - x[0] + 1) * x[1])

        return area

tests = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([5, 5, 1, 7, 1, 1, 5, 2, 7, 6], 12),
    ([1, 1], 2),
    ([37], 37),
    ([3, 6, 5, 7, 4, 8, 1, 0], 20),
    ([0, 9], 9),
    ([9, 0], 9),
    ([0, 2, 1, 5, 6, 2, 3], 10),
    ([2, 1, 5, 6, 0, 2, 3], 10),
    ([2, 1, 5, 6, 2, 3, 0], 10),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
]

solution = Solution()
for test in tests:
    result = solution.largestRectangleArea(test[0])
    if result != test[1]:
        print(f"Failed test: {test}. Got {result}, expected: {test[1]}.")