class Solution:
    def isValid(self, s: str) -> bool:
        maptoString = {')':'(','}':'{',']':'['}
        stack = []

        for x in s:
            if x in maptoString:
                if stack and stack[-1] in maptoString[x] :
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        
        if stack:
            return False
        else:
            return True