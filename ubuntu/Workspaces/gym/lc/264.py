class Solution:

    def nthUglyNumber(self, n: int) -> int:

        x1, x2, x3 = 0, 0, 0
        
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            
            y1 = dp[x1] * 2
            y2 = dp[x2] * 3
            y3 = dp[x3] * 5

            dp[i] = min(y1, y2, y3)
            
            if dp[i] == y1:
                x1 += 1
            if dp[i] == y2:
                x2 += 1
            if dp[i] == y3:
                x3 += 1
                
        return dp[n-1]

print(Solution().nthUglyNumber(1))