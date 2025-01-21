# Q 36 VAlid Sudoku

class Solution(object):
    def isValidSudoku(self, board):
        if board is None:
            return True
        
        # Check rows
        for i in range(9):
            table = set()
            for j in range(9):
                curr = board[i][j]
                if curr != '.':
                    if curr in table:
                        return False
                    table.add(curr)
        
        # Check columns
        for j in range(9):
            table = set()
            for i in range(9):
                curr = board[i][j]
                if curr != '.':
                    if curr in table:
                        return False
                    table.add(curr)
        
        # Check 3x3 blocks
        for i in range(3):
            for j in range(3):
                table = set()
                for k in range(9):
                    curr = board[i * 3 + k // 3][j * 3 + k % 3]
                    if curr != '.':
                        if curr in table:
                            return False
                        table.add(curr)
        
        return True
