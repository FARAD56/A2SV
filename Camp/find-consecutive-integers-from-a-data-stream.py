from collections import defaultdict
class DataStream(object):

    def __init__(self, value, k):
        self.val = value
        self.head = self.tail = None
        self.maxsize = k
        self.Dict = defaultdict(int)
        self.set = set()
        self.size = 0

    def op(self,num):
        self.size += 1
        self.Dict[num] += 1
        self.set.add(num)
    
    def update(self,num):
        self.Dict[num] -=1
        if self.Dict[num] == 0:
            self.set.remove(num)

    def check(self):
        if len(self.set) > 0:
            popped = self.set.pop()
            self.set.add(popped)
            if self.size == self.maxsize and len(self.set) == 1 and popped == self.val:
                return True

    def addHead(self,newnode):
        self.head = newnode
        self.tail = newnode

    def addNode(self,newnode):
        self.head.next = newnode
        self.head = self.head.next


    def consec(self, num):
        newnode = ListNode(num)
        if not self.head:
            self.addHead(newnode)
            self.op(num)
            return self.check()

        if self.maxsize == 1:
            return True if num == self.val else False

        if self.size < self.maxsize:
            self.addNode(newnode)
            self.op(num)
            return self.check()
        else:
            if self.tail:
                val = self.tail.val
                self.update(val)
                self.tail = self.tail.next
                self.size -= 1
            self.addNode(newnode)
            self.op(num)
            return self.check()
            
    
        
class ListNode:
    def __init__(self,val = None):
        self.val = val
        self.next = None


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)