class Solution:

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [2, 3, 5]
        for f in factors:
            while n % f == 0:
                n //= f

        return True if n == 1 else False
            
print(Solution().isUgly(0))