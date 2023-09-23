class Solution(object):
    def insertionSortList(self, head):
        sorted_head = ListNode()
        sorted_head.next = head
        sorted_tail = head
        current = head.next

        while current:
            if sorted_tail.val <= current.val:
                sorted_tail = current
                current = current.next
            else:
                moving = sorted_head
                sorted_tail.next = current.next

                while moving.next.val < current.val:
                    moving = moving.next

                current.next = moving.next
                moving.next = current
                current = sorted_tail.next

        return sorted_head.next 
        