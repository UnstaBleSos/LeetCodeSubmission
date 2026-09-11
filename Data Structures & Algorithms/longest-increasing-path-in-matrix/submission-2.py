class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        length = 0 
        rows  = len(matrix)
        cols = len(matrix[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        dp = [[0]* (cols) for _ in range(rows)]
        def dfs(row,col):
            
            if dp[row][col] != 0:
                return dp[row][col]
            
            best = 1 
            for r,c in dirs:
                nr = row+r
                nc = col+c

                if nr>= rows or nc >= cols or nr<0 or nc <0:
                    continue 
                
                if matrix[nr][nc] > matrix[row][col]:
                    candidate = 1 + dfs(nr,nc)

                    best = max(best, candidate)

            dp[row][col] = best
            return best 
            

        for i in range(rows):
            for j in range(cols):
                length = max(length,dfs(i,j))
        
        return length


