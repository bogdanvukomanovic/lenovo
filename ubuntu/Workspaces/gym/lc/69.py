class Solution:

    def mySqrt(self, x: int) -> int:

        lb, ub = 0, x

        while lb <= ub:

            m = lb + (ub - lb) // 2
 
            if m ** 2 == x:
                return m

            if m ** 2 < x: 
                lb = m + 1
            else: 
                ub = m - 1

        return ub

print(Solution().mySqrt(8))
