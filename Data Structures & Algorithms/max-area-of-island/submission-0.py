class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row,col = len(grid), len(grid[0])
        path = set()
        maxArea = 0
        area = 1
        def dfs(r,c):
            if r>= row or c>= col or r<0 or c<0:
                return 0
            if grid[r][c] == 0:
                return 0
            if (r,c) in path:
                return 0
            path.add((r,c))
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
                if (i,j) in path:
                    continue
                area = dfs(i,j)
                maxArea = max(maxArea , area)
        return maxArea