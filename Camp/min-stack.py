class MinStack(object):

    def __init__(self):
        self.array = []
        

    def push(self, val):
        self.array += [val]
        

    def pop(self):
        if len(self.array) > 0:
            value = self.array[-1]
            self.array = self.array[:-1]
            return value
        

    def top(self):
        return self.array[-1]
        

    def getMin(self):
        mini = float("inf")
        for num in self.array:
            mini = min(mini,num)
        return mini        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()