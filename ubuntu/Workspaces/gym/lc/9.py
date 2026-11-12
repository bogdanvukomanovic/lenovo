class Solution:

    # def isPalindrome(self, x: int) -> bool:
        
    #     x = str(x)

    #     for i in range(0, len(x) // 2):
        
    #         if not x[i] == x[-1-i]:
    #             return False

    #     return True
    
    # def isPalindrome(self, x: int) -> bool:
    #     x = str(x)
    #     return x[::-1] == x
    
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
  
        t, y = x, 0
        
        while t > 0:
            y = y * 10 + t % 10
            t = t // 10 

        return x == y


x = -210012
print(Solution().isPalindrome(x))