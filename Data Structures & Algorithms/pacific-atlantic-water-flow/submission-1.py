class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        row, col = len(heights), len(heights[0])
        atlantic = [[False]* col for _ in range(row)]
        pacific = [[False]* col for _ in range(row)]
        drs = [(1,0),(-1,0),(0,1),(0,-1)]
        output = []
        def dfs(r,c,ocean):
            if ocean[r][c]:
                return 
            ocean[r][c] = True
            for dr, dc in drs:
                nr = dr+r
                nc = dc+c

                if nr>=row or nc>=col or nr<0 or nc<0:
                    continue
                
                if heights[r][c] <= heights[nr][nc]:
                    dfs(nr,nc,ocean)
            
        
        for i in range(col):
            dfs(0,i,pacific)

        for j in range(row):
            dfs(j,0,pacific)
        
        for i in range(col):
            dfs(row-1,i,atlantic)
        
        for j in range(row):
            dfs(j,col-1,atlantic)

        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    output.append([i,j])

        return output
        