class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        row, col = len(grid), len(grid[0])
        q= deque()
        fresh = 0
        minute=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            didRot = False
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr = dr+r
                    nc = dc+c

                    if nr>=row or nc>= col or nc<0 or nr<0:
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        didRot = True
                        fresh-=1
                        q.append((nr,nc))
            if didRot:
                minute+=1
        
        if fresh == 0:
            return minute
        else:
            return -1
                