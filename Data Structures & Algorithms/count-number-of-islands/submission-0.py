class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row,col = len(grid) , len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r,c):
            if r<0 or c<0:
                return 
            
            if r>=row or c>= col:
                return 
            
            if grid[r][c] == "0":
                return
            
            if (r,c) in visited:
                return

            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    continue
                if (i,j) in visited:
                    continue
                dfs(i,j)
                islands+=1
        return islands