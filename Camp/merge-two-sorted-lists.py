# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = Nhead = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                Nhead.next = list1
                list1 = list1.next
            else:
                Nhead.next = list2
                list2 = list2.next
            Nhead = Nhead.next

        if list2:
            Nhead.next = list2
            list2 = Nhead
        if list1:
            Nhead.next = list1
            list1 = Nhead
        
        return head.next




