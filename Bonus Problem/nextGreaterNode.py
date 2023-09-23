class Solution(object):
    def nextLargerNodes(self, head):
        arr = []
        stack = []
        curr = head
        i = 0
        while curr:
            
            while stack and stack[-1][0] < curr.val:
                arr[stack[-1][1]] = curr.val
                stack.pop()

            stack.append((curr.val,i))
            arr.append(0)
            i += 1
            curr = curr.next
        return arr
        