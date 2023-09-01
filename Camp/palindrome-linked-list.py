class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        current = head
        while current and prev:
            if current.val != prev.val:
                return False
            current, prev = current.next,prev.next
        return True
        
        
        