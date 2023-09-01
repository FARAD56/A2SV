class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if not self.head:
            return -1
        current = self.head
        while current and index > 0:
            current = current.next
            index -= 1
        return current.value if current else -1

        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode = Node(val)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
        
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return

        if not self.head:
            return

        current = self.head
        newnode = Node(val)
        while current and index > 1:
            current = current.next
            index -= 1

        if current != None and index == 1:
            newnode.next = current.next
            current.next = newnode

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        while current and index > 1:
            current = current.next
            index -= 1
        if index == 1 and current and current.next:
            current.next = current.next.next
        

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)