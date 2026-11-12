from typing import List

class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        nums += nums

        result = [-1] * 2 * n
        monotonic_stack = []

        for i, x in enumerate(nums):

            while monotonic_stack and x > monotonic_stack[-1][1]:

                result[monotonic_stack[-1][0]] = x
                monotonic_stack.pop()

            monotonic_stack.append((i, x))

        return result[:n]
    
nums = [1, 8, -1, -100, -1, 222, 1111111, -111111]
print(Solution().nextGreaterElements(nums))