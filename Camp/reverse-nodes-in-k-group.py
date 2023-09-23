class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode()
        start = dummy
        end = dummy
        track = dummy
        end_next = head

        dummy.next = head

        current = head
        length = 1
        while current:
            length += 1
            current = current.next

        while length > k:
            start = end_next
            itr = k
            while itr:
                end = end_next
                end_next = end_next.next
                itr -= 1

            prev = None
            curr = start
            while curr != end_next:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            track.next = prev
            track = start

            length -=k
        track.next = end_next

        return dummy.next

        