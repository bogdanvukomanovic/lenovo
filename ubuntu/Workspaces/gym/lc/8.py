class Solution:
    
    def myAtoi(self, xs: str) -> int:
        
        xs = xs.strip()
        
        if len(xs) == 0 or xs == "-" or xs == "+" or xs[:2] == "+-" or xs[:2] == "-+":
            return 0

        sign = 1

        if xs[0] == '-':
            sign = -1
            xs = xs[1:]

        if xs[0] == '+':
            sign = 1
            xs = xs[1:]

        if not xs[0].isdigit():
            return 0
        
        i, n = 0, len(xs)
        while i < n and xs[i].isdigit():
            i += 1

        xs = xs[:i]

        n = len(xs)
        number, d = 0, 1
        for i in range(n - 1, -1, -1):
            number += int(xs[i]) * d
            d *= 10
        
        return max(-2**31, min(2**31 - 1, sign * int(xs)))
    
xs = "-+12"
print(Solution().myAtoi(xs))