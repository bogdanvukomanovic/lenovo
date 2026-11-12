from typing import List

class Solution:

    def f(self, coins: List[int], amount: int, dp: {int: int}):

        if amount in dp:
            return dp[amount]

        dp[amount] = float("inf")
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + self.f(coins, amount - coin, dp))

        return dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if not amount:
            return 0

        dp = {}
     
        for coin in coins:
            dp[coin] = 1
        
        return dp[amount] if self.f(coins, amount, dp) != float("inf") else -1 


coins, amount = [1, 2, 5], 11
# coins, amount = [2], 3
# coins, amount = [1], 0
print(Solution().coinChange(coins, amount))