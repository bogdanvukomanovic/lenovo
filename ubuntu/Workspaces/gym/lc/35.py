from typing import List

class Solution:
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums) - 1
        lb = 0
        ub = n
        
        if n == 0:
            return 0 if target <= nums[0] else 1

        while lb < ub:
 
            m = (ub - lb) // 2 + lb
            
            if target < nums[m]:
                ub = m
            else:
                lb = m + 1
        
            if target == nums[ub]:
                return ub
            
            if target == nums[lb]:
                return lb
            
            if target == nums[m]:
                return m

        return ub + 1 if target > nums[ub] else ub

tests = [
    [([1,3,5,6], 4),  2],
    [([1,3,5,6], 5),  2],
    [([1,3,5,6], 2),  1],
    [([1,3,5,6], 7),  4],
    [([1,3], -1),  0],
    [([1,3], 2),  1],
    [([1,3], 4),  2]
]

solution = Solution()
for test in tests:
    x = solution.searchInsert(test[0][0], test[0][1])
    if x != test[1]:
        print("Wrong result (", x, ") for test:", test)


def searchInsert(nums: List[int], target: int) -> int:
    
    # ub = len(nums) - 1 
    
    lb = 0
    ub = len(nums) 

    while lb < ub:
        m = (ub - lb) // 2 + lb
        if target > nums[m]:
            lb = m + 1
        else:
            ub = m

    return lb

print(searchInsert([1], 2))