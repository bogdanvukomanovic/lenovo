class Solution:
    
    def lengthOfLastWord(self, s: str) -> int:

        result = 0
        for i in range(len(s)-1, -1, -1):
            if not result and s[i] == ' ':
                continue
            if result and s[i] == ' ':
                break
            result += 1
        
        return result
    
    # def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split()[-1])

s = "Hello World"
print(Solution().lengthOfLastWord(s))