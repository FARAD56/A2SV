class Solution(object):
    def addTwoNumbers(self, l1, l2):
 
        head = Dhead = ListNode(0)
        sumi = remain = 0

        while l1 or l2 or remain!= 0:
            if l1:
                remain += l1.val
                l1 = l1.next
            if l2:
                remain += l2.val
                l2 = l2.next

            Dhead.next = ListNode(remain%10)
            Dhead = Dhead.next

            remain //= 10
                
        return head.next
    