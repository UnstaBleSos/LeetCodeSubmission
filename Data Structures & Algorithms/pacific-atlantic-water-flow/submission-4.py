class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        row, col = len(heights), len(heights[0])
        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        output = []

        def dfs(r,c,oceans):
            if oceans[r][c] == True:
                return
            
            oceans[r][c] = True
            for dr,dc in dirs:
                nr = dr+r
                nc = dc+c

                if nr>=row or nc>=col or nc<0 or nr<0:
                    continue
                
                if heights[r][c] <= heights[nr][nc]:
                   dfs(nr,nc,oceans)
        
        for i in range(col):
            dfs(0,i,pacific)
        
        for j in range(row):
            dfs(j,0,pacific)
        
        for i in range(col):
            dfs(row-1,i,atlantic)
        
        for j in range(row):
            dfs(j, col-1, atlantic)
        
        for i in range(row):
            for j in range(col):
                if atlantic[i][j] and pacific[i][j]:
                    output.append([i,j])

        return output
        
        
