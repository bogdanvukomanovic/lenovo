from typing import List

class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])

        lb, ub = 0, (m * n) - 1 

        while lb <= ub:
             
            mid = lb + (ub - lb) // 2
            
            if matrix[mid//n][mid%n] == target:
                return True

            if matrix[mid//n][mid%n] < target:
                lb = mid + 1
            else:
                ub = mid - 1

        return False

matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 8
print(Solution().searchMatrix(matrix, target))
