class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*","/"]
        stack = []
        result = 0 
        for x in range(len(tokens)):
           try:  
            stack.append(int(tokens[x]))
           except ValueError:
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
                result =int( first / second)
                stack.append(result)
        return stack[-1]


            
        
        
                