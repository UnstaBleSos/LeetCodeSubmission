class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            freq=set()
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                if board[i][j]  in freq:
                   return False
                freq.add(board[i][j])

        for i in range(cols):
            freq=set()
            for j in range(rows):
                if board[j][i] == ".":
                    continue
                if board[j][i]  in freq:
                   return False
                freq.add(board[j][i])

        for i in range(0,rows,3):
            seen = set()
            for j in range(0,cols,3):
                for c in range(i,i+3):
                    for d in range(j,j+3):
                        if board[c][d] == ".":
                            continue
                        if board[c][d] in seen:
                            return False
                        seen.add(board[c][d]) 
        return True