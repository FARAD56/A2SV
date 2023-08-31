# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newnode = ListNode(-1)
        prev = None
        current = head
        while current:
            newnode.next = current.next
            current.next = prev
            prev = current
            current = newnode.next
        return prev
