class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return [[]]
        path = []
        columnsUsed = set()
        leftdiagonal = set()
        rightdiagonal = set()
        res = []
        def backTrack(r):
            if r == n:
                rows = []
                for value in path:
                    dots = ['.']*n
                    dots[value] = "Q"
                    rows.append("".join(dots))
                res.append(rows)
                return 

            for c in range(n):
                if c in columnsUsed or (r-c) in leftdiagonal or (r+c) in rightdiagonal:
                    continue

                columnsUsed.add((c))
                leftdiagonal.add((r-c))
                rightdiagonal.add((r+c))

                path.append(c)
                backTrack(r+1)
                path.pop()
                columnsUsed.remove(c)
                leftdiagonal.remove((r-c))
                rightdiagonal.remove((r+c))
        
        backTrack(0)
        return res 
        
        
        

            
