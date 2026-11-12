from typing import List

class Solution:

    def sweep(self, i: int, nums: List[int], n: int, target: int) -> List[int]:

        first, last = i, i
        while first > 0 and nums[first] == target:
           first -= 1
        while last < n and nums[last] == target:
            last += 1

        first = i if first == i else first + 1
        last = i if last == i else last - 1

        return [first, last]


    def searchRange(self, nums: List[int], target: int) -> List[int]:

        result = [-1, -1]

        n = len(nums)
        lb, ub = 0, n - 1

        while lb <= ub:

            m = lb + (ub - lb) // 2
            if nums[m] == target:
                result = self.sweep(m, nums, n, target)

            if nums[m] < target:
                lb = m + 1
            else:
                ub = m - 1

        return result

nums, target = [5, 7, 7, 8, 8, 10], 8
print(Solution().searchRange(nums, target))
