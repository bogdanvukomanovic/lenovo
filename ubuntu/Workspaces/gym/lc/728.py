from typing import List

class Solution:

    def check(self, n: int) -> bool:

        x = n

        while x > 0:

            d = x % 10

            if d == 0 or n % d:
               return False

            x //= 10

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [n for n in range(left, right + 1) if self.check(n)]

print(Solution().selfDividingNumbers(47, 85))
