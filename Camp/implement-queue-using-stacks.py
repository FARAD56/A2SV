class MyQueue(object):

    def __init__(self):
        self.head = []
        
    def push(self, x):
        self.head.append(x)

    def pop(self):
        val = self.head[0]
        self.head = self.head[1:]
        return val
        

    def peek(self):
        return self.head[0]
        

    def empty(self):
        if len(self.head) > 0:
            return False
        else:
            return True
        
class ListNode:
    def __init__(self,val = None):
        self.val = val
        self.next = None

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()