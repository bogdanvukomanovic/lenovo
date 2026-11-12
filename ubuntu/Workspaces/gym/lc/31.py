from typing import List

class Solution:

    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)

        i = n - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i < 0:
            nums.reverse()
            return

        j = n - 1
        while nums[i] >= nums[j]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:n] = nums[n:i:-1]

nums = [1, 6, 5, 4, 3, 1]
nums = [3, 2, 1]
nums = [2, 3, 1]
Solution().nextPermutation(nums)
print(nums)
