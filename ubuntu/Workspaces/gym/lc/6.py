class Solution:

    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        result = [""] * numRows

        i, n = 0, len(s)
        
        position = 0 
        direction = 1

        while i < n:
            
            result[position] += s[i]
            
            position += direction
            i += 1
            
            if i % (numRows - 1) == 0:
                direction *= -1 

        return "".join(result)

s, numRows = "PAYPALISHIRING", 4
print(Solution().convert(s, numRows))