from typing import List

class Solution:

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def sweep(board: List[List[str]], m: int, n: int, i: int, j: int) -> int:
            
            XYS   = set([(-1, -1), (-1, 0), (-1, 1),
                         (0,  -1),          (0,  1),
                         (1,  -1), (1,  0), (1,  1)])

            UP    = set([(-1, -1), (-1, 0), (-1, 1)])
            DOWN  = set([(1,  -1), (1,  0), (1,  1)])
            LEFT  = set([(-1, -1), (0, -1), (1, -1)])
            RIGHT = set([(-1,  1), (0,  1), (1,  1)])
            
            if i == 0: XYS -= UP
            if i == m: XYS -= DOWN
            if j == 0: XYS -= LEFT 
            if j == n: XYS -= RIGHT 

            XYS = list(XYS)
     
            mines = 0
            for xy in XYS:
                if board[i + xy[0]][j + xy[1]] == 'M':
                    mines += 1

            if mines == 0:
                board[i][j] = 'B'
                for xy in XYS:
                    if board[i + xy[0]][j + xy[1]] == 'E':
                        board = sweep(board, m, n, i + xy[0], j + xy[1])
                return board
            else:
                board[i][j] = str(mines)
                return board         
        
        m, n = len(board) - 1, len(board[0]) - 1

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        return sweep(board, m, n, click[0], click[1])

# board = [["E","E","E","E","E"],
#          ["E","E","M","E","E"],
#          ["E","E","E","E","E"],
#          ["E","E","E","E","E"]]
# click = [3, 0]

board = [["E"], ["E"], ["E"], ["E"]]
click = [0, 0]
print(Solution().updateBoard(board, click))