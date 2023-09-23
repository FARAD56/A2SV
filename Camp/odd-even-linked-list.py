class Solution(object):
    def oddEvenList(self, head):
        ehead = even = ListNode()
        Ohead = odd = ListNode()
        current = head
        count = 1
        while current:
            if count % 2 == 0:
                even.next = current
                even = even.next
            else:
                odd.next = current
                odd = odd.next
            count +=1
            current = current.next

        even.next = None

        odd.next = ehead.next
        return Ohead.next 
        
        