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
        minstack = [1]*len(self.stack)
        for x in range(len(self.stack)):
            if not minstack:
                minstack[x] = self.stack[x]

            if self.stack[x] < minstack[x]:
                minstack[x] = self.stack[x]
            

        return minstack[-1]

