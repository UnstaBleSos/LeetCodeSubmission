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
        freq={}
        min = float('inf')
        for x in range(len(self.stack)):
            freq[x] = self.stack[x]
            if freq[x] < min:
                min= freq[x]

        return min

