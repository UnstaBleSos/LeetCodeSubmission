class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*","/"]
        stack = []
        result = 0 
        for x in range(len(tokens)):
           if tokens[x].isdigit(): 
            stack.append(int(tokens[x]))
           if tokens[x] in operands:
            second = stack.pop()
            first = stack.pop()
            if tokens[x] =='+':
                result = first + second
                stack.append(result)
            elif tokens[x] == '-':
                result = first - second
                stack.append(result)
            elif tokens[x] == '*':
                result = first * second
                stack.append(result)
            elif tokens[x] == '/':
                result = first / second
                stack.append(result)
        return stack[-1]


            
        
        
                