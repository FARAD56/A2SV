# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            Dummy = ListNode()
            dhead = Dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    dhead.next = l1
                    l1 = l1.next
                else:
                    dhead.next = l2
                    l2 = l2.next
                dhead = dhead.next

            if l1:
                dhead.next = l1
            if l2:
                dhead.next = l2

            return Dummy.next
                
        All = None
        for i in range(len(lists)):
            All = merge(lists[i], All)

        return All



