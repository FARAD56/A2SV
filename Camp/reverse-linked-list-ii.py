class Solution(object):
    def reverseBetween(self, head, left, right):
        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next

        l = left - 1
        r = right -1

        while l < r:
            arr[l],arr[r] = arr[r], arr[l]
            l+=1
            r-=1
        
        Dum = dummy = ListNode()

        for num in arr:
            dummy.next = ListNode(num)
            dummy = dummy.next

        return Dum.next

            
            
                