class MyStack(object):

    def __init__(self):
        self.head = None
        

    def push(self, x):
        newnode = ListNode(x)
        if not self.head:
            self.head = newnode
            return
        newnode.next = self.head
        self.head = newnode
        

    def pop(self):
        if not self.head:
            return
        val = self.head.val
        self.head = self.head.next
        return val
        

    def top(self):
        if not self.head:
            return
        return self.head.val 
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.head:
            return True
        return False

class ListNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()