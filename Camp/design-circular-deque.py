class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.deque = []
        self.maxsize = k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.maxsize:
            self.deque.insert(0,value)
            return True
        else:
            return False
        
        
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.maxsize:
            self.deque.append(value)
            return True
        else:
            return False
        

    def deleteFront(self):
        if len(self.deque) > 0:
            self.deque = self.deque[1:]
            return True
        else:
            return False
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque = self.deque[:-1]
            return True
        else:
            return False
        

    def getFront(self):
        """
        :rtype: int
        """
        return self.deque[0] if len(self.deque) > 0 else -1
        

    def getRear(self):
        """
        :rtype: int
        """
        return self.deque[-1] if len(self.deque) > 0 else -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return True if len(self.deque) == 0 else False
        

    def isFull(self):
        """
        :rtype: bool
        """
        return True if len(self.deque) == self.maxsize else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()