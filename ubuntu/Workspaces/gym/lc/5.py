class Solution:

    # def longestPalindrome(self, s: str) -> str:
        
    #     result = [0, 1]

    #     n = len(s)

    #     dp = [[0] * n for _ in s]
    #     for i in range(n):
    #         dp[i][i] = 1
        
    #     d = 0
    #     while d < n - 1:

    #         i = 0
    #         j = d + 1 
            
    #         while j < n:
                
    #             if j == i + 1:
    #                 dp[i][j] = 2 if s[j-1] == s[j] else 0
    #             else:

    #                 if i < 0 and dp[i][j-1] > 0:
    #                     if s[i-1] == s[j]:
    #                         dp[i][j] = j - i + 1
    #                 else:
    #                     if s[i] == s[j] and dp[i+1][j-1] > 0:
    #                         dp[i][j] = j - i + 1

    #             if dp[i][j] > result[1]:
    #                 result = [i, dp[i][j]]

    #             i += 1
    #             j += 1

    #         d += 1

    #     return s[result[0]:result[0] + result[1]]

    def longestPalindrome(self, s: str) -> str:
        
        result = [0, 1]
        n = len(s)

        dp = [[0] * n for _ in s]
        for i in range(n):
            dp[i][i] = 1
        
        d = 0
        while d < n - 1:

            i = 0
            j = d + 1 
            
            while j < n:
                
                if j == i + 1:
                    dp[i][j] = 2 if s[j-1] == s[j] else 0
                elif dp[i+1][j-1] > 0 and s[i] == s[j]:
                        dp[i][j] = j - i + 1 

                if dp[i][j] > result[1]:
                    result = [i, dp[i][j]]

                
                i += 1
                j += 1

            d += 1

        return s[result[0]:result[0] + result[1]]

print(Solution().longestPalindrome("ABBA"))