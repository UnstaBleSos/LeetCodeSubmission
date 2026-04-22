class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return None
        matchExp = ["+","-","*","/"]
        stack = []
        for x in tokens:
            if x not in matchExp:
                stack.append(int(x))
                print(stack)
            if x == '+':
                second = stack.pop()
                first = stack.pop()
                result = first + second
                stack.append(result)
            elif x == '-':
                second = stack.pop()
                first = stack.pop()
                result = first -second
                stack.append(result)
            elif x == '*':
                second = stack.pop()
                first = stack.pop()
                result = first * second
                stack.append(result)
            elif x == '/':
                second = stack.pop()
                first = stack.pop()
                result = first / second
                stack.append(int(result))
        return stack[-1]