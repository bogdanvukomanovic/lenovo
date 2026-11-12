from typing import List

import math

class Solution:

    def f(self, piles: List[int], h: int, k: int) -> bool:

        for p in piles:
            h -= (math.ceil(p / k))

            if h < 0:
                return False

        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lb, ub = 1, max(piles) * len(piles)

        while lb < ub:

            m = lb + (ub - lb) // 2
            if self.f(piles, h, m):
                ub = m
            else:
                lb = m + 1

        return lb

piles, h = [30, 11, 23, 4, 20], 5
piles, h = [805306368, 805306368, 805306368], 1_000_000_000
print(Solution().minEatingSpeed(piles, h))
