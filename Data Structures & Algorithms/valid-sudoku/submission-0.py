class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in board:
            rows = set()
            for j in i:
                if j == ".":
                    continue
                if j in rows:
                    return False
                rows.add(j)
        
        # Check columns
        for i in range(len(board[0])):
            cols = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in cols:
                    return False
                cols.add(board[j][i])
        
        # Check squares
        for i in range(9):
            square = set()
            for j in range(3):
                for k in range(3):
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in square:
                        return False
                    square.add(board[row][col])

        return True
