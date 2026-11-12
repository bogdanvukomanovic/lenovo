import math

from typing import List

class Solution:

    def getRow(self, n: int) -> List[int]:
       
        xs = []

        for k in range(n // 2 + 1):
            xs.append(int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))    

        return xs + xs[0:n//2][::-1] if n % 2 == 0 else xs + xs[0:n//2+1][::-1]

print(Solution().getRow(33))