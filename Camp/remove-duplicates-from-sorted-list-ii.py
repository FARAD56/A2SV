class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return

        Dict = defaultdict(int)

        current = head
        while current:
            Dict[current.val] += 1
            current = current.next

        current = head

        while current.next:
            if Dict[current.next.val] > 1:
                current.next = current.next.next
            else:
                current = current.next

        if Dict[head.val] > 1:
            head = head.next

        return head
