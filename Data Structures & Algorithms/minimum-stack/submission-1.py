class MinStack:
    def __init__(self):
        self.stack = []
        self.length = 0
        self.minstack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length += 1
        if (self.min > val):
            self.min = val
        self.minstack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.length -= 1
        self.minstack.pop()
        if (self.length <= 0):
            self.min = float('inf')
        else:
            self.min = self.minstack[self.length - 1]

    def top(self) -> int:
        return self.stack[self.length - 1]

    def getMin(self) -> int:
        return self.min
