class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return []
        
        row, col = len(board), len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        def dfs(r,c):
            if board[r][c] == "X":
                return

            if ((r,c)) in visited:
                return
            visited.add((r,c))

            
            for dr, dc in dirs:
                nr = dr+r
                nc = dc+c

                if nr>=row or nc>=col or nc<0 or nr<0:
                    continue
                
                if board[nr][nc] == 'O':
                    dfs(nr,nc)
        
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 or i == row-1 or j==col-1:
                    dfs(i,j)
        

        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'
           
            