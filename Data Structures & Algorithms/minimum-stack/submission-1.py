class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # self.stack.pop()
        

        # python evaluates the condition inside if
        # to do that it must execute self.stack.pop()
        # that removes and returns the top elements
        # then compares it to self.minStack[-1]
        # so... self.stack.pop() always run, regardless of whether the conditions is True or False
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]