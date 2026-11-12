class Solution:

    def romanToInt(self, s: str) -> int:
        
        hash = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        i, integer, number = 0, 0, 0
        while i < len(s):
            
            number = hash[s[i]]
            if i < len(s) - 1 and number < hash[s[i+1]]:
                number = hash[s[i+1]] - number
                i += 1     

            integer += number

            number = 0
            i += 1

        return integer

print(Solution().romanToInt("MCMXCVIII"))