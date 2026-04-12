class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min = float('inf')
        for x in range(len(self.stack)):
           if self.stack[x] < min:
            min= self.stack[x]

        return min

