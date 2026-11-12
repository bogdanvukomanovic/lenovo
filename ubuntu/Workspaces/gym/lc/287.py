from typing import List

class Solution:

    # Floyds Cycle Detection algorithm
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

nums = [1, 3, 4, 2, 2]
nums = [3, 1, 3, 4, 2]
print(Solution().findDuplicate(nums))
