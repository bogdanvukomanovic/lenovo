from typing import List

class Solution:

    def maxCoins(self, piles: List[int]) -> int:

        piles.sort(reverse = True)

        result, n = 0, len(piles) // 3

        for i in range(0, n):
            result += piles[i * 2 + 1]

        return result

piles = [2, 4, 1, 2, 7, 8]
print(Solution().maxCoins(piles))
