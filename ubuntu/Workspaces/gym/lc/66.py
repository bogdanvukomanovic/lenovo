from typing import List

class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            
            if carry == 0:
                break

            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = 1 if sum > 9 else 0
        
        if carry == 1:
            digits.insert(0, 1)

        return digits
            
    def f(self, digits: List[int], add: int) -> List[int]:
        
        if add == 0:
            return digits
        
        if len(digits) == 0 and add == 0:
            return digits
        
        if len(digits) == 0 and add == 1:
            return [1]
    
        sum = digits[-1] + add
        return self.f(digits[0:-1], sum // 10) + [sum % 10]




digits = [9,9,9,9,9,9]
print(Solution().plusOne(digits))
# print(Solution().f(digits, 1))
