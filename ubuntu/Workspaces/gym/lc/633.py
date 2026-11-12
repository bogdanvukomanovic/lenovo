import math

class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        
        lb = 0
        ub = math.floor(math.sqrt(c))

        while lb <= ub:
            
            x = lb**2 + ub**2

            if x > c:
                ub -= 1 
            elif x < c:
                lb += 1
            else:
                return True
        
        return False
            
print(Solution().judgeSquareSum(818))