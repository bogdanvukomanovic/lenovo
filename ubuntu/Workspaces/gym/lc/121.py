from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        result = 0
        m = prices[n-1]
        for i in range(n - 2, -1, -1):

            if m - prices[i] < result:
                m = max(m, prices[i])
            else:
                result = m - prices[i]

        return result

prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))