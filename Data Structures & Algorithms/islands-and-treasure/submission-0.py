class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []
        
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))
        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                newr = dr+r
                newc = dc+c 

                if newr>=row or newc >=col or newr<0 or newc<0:
                    continue
                
                if grid[newr][newc] == 2147483647:
                    grid[newr][newc] = grid[r][c] + 1 
                    q.append((newr,newc))
                
            

               
                