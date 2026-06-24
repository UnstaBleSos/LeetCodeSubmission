class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        row,col = len(board), len(board[0])

        path = set()

        def dfs(r,c, index):
            if index == len(word):
                return True

            if r<0 or c<0:
                return False

            if r >= row:
                return False
            
            if c >= col:
                return False
            
            if board[r][c] != word[index]:
                return False
            
            if (r,c) in path:
                return False
            
            path.add((r,c))
            
            found = (
                dfs(r+1,c,index+1) or
                dfs(r-1,c,index+1) or
                dfs(r,c+1,index+1) or
                dfs(r,c-1,index+1) 
            )
            path.remove((r,c))

            return found

        for i in range(row):
            for j in range(col):
                
                if dfs(i,j,0):
                    return True
            
        return False