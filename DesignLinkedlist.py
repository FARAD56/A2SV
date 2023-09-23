class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedlist:

    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

    def addAtTail(self, val):
        newnode = Node(val)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    def get(self, index):
        if not self.head:
            return
        current = self.head
        while current and index:
            current = current.next
            index -= 1
        return current.val if current else -1

    def printList(self):
        if not self.head:
            return
        lis = ""
        current = self.head
        while current.next:
            lis += f'{current.val} -> '
            current = current.next
        lis += f'{current.val}'
        print(lis)

    def deleteAtIndex(self, index):
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
        return

    def addAtIndex(self, index, val):
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

        if current and index == 1:
            newnode.next = current.next
            current.next = newnode




obj = MyLinkedlist()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.printList()
obj.deleteAtIndex(2)
print(obj.get(1))
obj.deleteAtIndex(1)
obj.printList()
print(obj.get(1))
obj.printList()
print(obj.get(3))
obj.deleteAtIndex(3)
obj.printList()
obj.deleteAtIndex(0)
print(obj.get(0))
obj.deleteAtIndex(0)
print(obj.get(0))

if not head or not head.next:
    return head

second = obj.head
first = obj.head.next
dummy = ListNode()
head = dummy
while first or second:
    dummy.next = first
    first = first.next.next
    dummy.next = second
    second = second.next.next

