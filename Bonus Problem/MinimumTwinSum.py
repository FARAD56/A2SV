# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
            
        max_twin = float("-inf")
        while head or prev:
            if prev:
                val = prev.val
                prev = prev.next
            else:
                val = 0
            max_twin = max((head.val + val),max_twin)
            head = head.next

        return max_twin

        