# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1, l2):
            Dummy = ListNode()
            dhead = Dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    dhead.next = l1
                    l1 = l1.next
                else:
                    dhead.next = l2
                    l2 = l2.next
                dhead = dhead.next

            if l1:
                dhead.next = l1
            if l2:
                dhead.next = l2
            return Dummy.next

        def msort(head):
            if not head or not head.next:
                return head
            current = head

            slow = head
            prev = head
            fast = head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None

            return merge(msort(current),msort(slow))
        
        return msort(head)
