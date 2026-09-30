class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        element = self.stack.pop()
        if element == self.min:
            if not self.stack:
                self.min = float('inf')
            else:
                self.min = min(self.stack)

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
