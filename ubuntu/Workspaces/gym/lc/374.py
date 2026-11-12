class Solution:

    pick = 42

    def guessNumber(self, n: int) -> int:
        
        def guess(num: int) -> int:

            if num == self.pick:
                return 0
            if num > self.pick:
                return -1
            if num < self.pick:
                return 1

        lb, ub = 1, n
        while lb < ub:
            
            m = lb + (ub - lb) // 2
            
            if guess(m) == 0:
                return m

            if guess(m) == -1:
                ub = m - 1
            else:
                lb = m + 1
        
        return lb

print(Solution().guessNumber(100))
