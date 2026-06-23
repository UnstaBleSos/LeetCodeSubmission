class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 0:
            return None
        
        res = []
        path = []
        def dfs(openings,closing):
            if len(path) == 2*n:
                res.append("".join(path.copy()))
                return

            if openings<n:
                path.append("(")
                dfs(openings+1,closing)
                path.pop()
            
            if closing<openings:
                path.append(")")
                dfs(openings,closing+1)
                path.pop()
        dfs(0,0)
        return res