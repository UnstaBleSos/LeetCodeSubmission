class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        area = 0 
        def dfs(r,c):
            if r<0 or c<0 or r>= row or c>= col:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            if (r,c) in visited:
                return 0

            visited.add((r,c))
            return 1+(
                dfs(r+1,c)+
                dfs(r-1,c)+
                dfs(r,c+1)+
                dfs(r,c-1)
            )

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                if (i,j) in visited:
                    continue
                area = dfs(i,j)
                maxArea = max(area, maxArea)
        
        return maxArea