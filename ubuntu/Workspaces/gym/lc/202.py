class Solution:
    
    def isHappy(self, n: int) -> bool:
            
            seen = set([n])
            
            while n > 1:

                x = 0

                while n > 0:
                    x += (n % 10) ** 2
                    n //= 10 

                if x in seen:
                    return False
                
                n = x                
                seen.add(n)
                
            return True

print(Solution().isHappy(2))

# TODO: https://en.wikipedia.org/wiki/Cycle_detection