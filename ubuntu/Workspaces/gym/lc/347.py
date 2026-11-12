from typing import List

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for num in nums:

            x = hash.setdefault(num, 0)
            hash[num] = x + 1

        return [y[0] for y in sorted(hash.items(), key = lambda x : x[1], reverse = True)][:k]

nums, k = [1, 1, 1, 2, 2, 3], 2
print(Solution().topKFrequent(nums, k))
