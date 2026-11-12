from typing import List

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        fresh, rotten = 0, []
        for i in range(m):
            for j in range(n):                
                if grid[i][j] == 2:
                    rotten.append((i, j))
                    grid[i][j] -= 2
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
            
        minute = -1
        while len(rotten) > 0:
            
            new = []

            for x in rotten:

                if grid[max(0, x[0] - 1)][x[1]] == 1:
                    new.append((x[0] - 1, x[1]))
                    grid[x[0] - 1][x[1]] -= 1

                if grid[x[0]][min(n - 1, x[1] + 1)] == 1:
                    new.append((x[0], x[1] + 1))
                    grid[x[0]][x[1] + 1] -= 1

                if grid[min(m - 1, x[0] + 1)][x[1]] == 1:
                    new.append((x[0] + 1, x[1]))
                    grid[x[0] + 1][x[1]] -= 1
                
                if grid[x[0]][max(0, x[1] - 1)] == 1:
                    new.append((x[0], x[1] - 1))
                    grid[x[0]][x[1] - 1] -= 1
                
            rotten = new
            minute += 1
                            
        return minute if sum(list(map(sum, grid))) == 0 else -1 
        
# grid = [[2,1,1],[0,1,1],[1,0,1]]
# grid = [[0,2]]
# grid = [[2,1,1],[1,1,1],[0,1,2]]
# grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[1,1],[1,1]]
print(Solution().orangesRotting(grid))    