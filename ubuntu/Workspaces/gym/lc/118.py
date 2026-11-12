from typing import List

class Solution:
    
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = [[] for _ in range(0, numRows)]

        for i, row in enumerate(result):
            for element in range(i+1):
                if element == 0 or element == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][element-1] + result[i-1][element])
        
        return result

solution = Solution()
print(solution.generate(7))

# Note that it was also possible to generate each element with binomial coefficient.