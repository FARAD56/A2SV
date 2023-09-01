class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return

        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        current = head
        index = length - n

        if index == 0:
            head = head.next

        while current and index > 1:
            current = current.next
            index -= 1
        if index == 1 and current and current.next:
            current.next = current.next.next

        return head


        
        