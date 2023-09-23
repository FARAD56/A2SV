class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or right == left:
            return head

        dummy = ListNode()
        lhead = dummy
        rhead = dummy
        mhead = dummy
        dummy.next = head
        for i in range(right+1):
            if i < left:
                mhead = lhead
                lhead = lhead.next
            rhead = rhead.next

        prev = None
        current = lhead
        while current!=rhead:
            next = current.next
            current.next = prev
            prev = current
            current = next

        mhead.next = prev
        lhead.next = rhead

        return dummy.next
            
            
                
