from typing import List


class Solution:

    def reverseString(self, xs: List[str]) -> None:

        n = len(xs)
        m = n // 2

        for i in range(m):
            xs[i], xs[n - 1 - i] = xs[n - 1 - i], xs[i]

        return xs


xs = ["H", "E", "L", "L", "O"]
xs = ["H", "E", "L", "L", "O", "!"]
print(Solution().reverseString(xs))
