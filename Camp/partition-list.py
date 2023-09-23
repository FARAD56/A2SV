class Solution(object):
    def partition(self, head, x):
        current = head
        lhead = left = ListNode()
        rhead = right = ListNode()

        while current:
            if current.val < x:
                left.next = current
                left = left.next
            else:
                right.next = current
                right = right.next 
            current = current.next
        right.next = None
        left.next = rhead.next
        
        return lhead.next
                