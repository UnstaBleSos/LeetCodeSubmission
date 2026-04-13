class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 :
            return False
        stack = []
        maptoclose = {')':'(',
        '}'
        :
        '{'
        ,
        ']'
        :
        '['
        }
        for x in s:
            if x in maptoclose:
                if stack and stack[-1] in maptoclose[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
                 
        return True
            
            
            


       

