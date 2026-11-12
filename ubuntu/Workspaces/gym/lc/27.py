from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
        
        return i


testcases = [
    [[3,2,2,3],         3, 2],
    [[0,1,2,2,3,0,4,2], 2, 5], 
    [[1,3,4,5,6],       2, 5],
    [[2,2,2,1,1,2,2,4], 2, 3],
    [[2,2,2,2,2,2,2,2], 2, 0],
    [[3,3,0],           5, 3],
    [[],                1, 0]
]

solution = Solution()

for test in testcases:

    x = solution.removeElement(test[0], test[1])
    
    if x != test[2]:
        print("For testcase", test, "got wrong result", x)