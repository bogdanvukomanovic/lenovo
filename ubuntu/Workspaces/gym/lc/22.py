from typing import List

class Solution:

    def f(self, n : int, dp: List[List[str]]) -> List[List[str]]:

        if dp[n-1] != []:
            return dp

        dp = self.f(n-1, dp)

        result = set(["(" + x + ")" for x in dp[n-2]])
        
        for i in range(1, n):
            
            for prefix in dp[i-1]:
                for sufix in dp[n-i-1]:

                    if (prefix + sufix) not in result:
                        result.add(prefix + sufix)
        
        dp[n-1] = list(result)

        return dp        
        
    def generateParenthesis(self, n: int) -> List[str]:
        
        dp = [[]] * n 
        dp[0] = ["()"]

        return self.f(n, dp)[n - 1]

print(Solution().generateParenthesis(9))