# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, str(root.val))])
        paths = []
        while queue:
            root, path = queue.popleft()

            if not root.left and not root.right:
                paths.append(path)

            if root.left:
                queue.append((root.left, path+str(root.left.val)))
            if root.right:
                queue.append((root.right, path+str(root.right.val)))

        sum_ = 0
        for path in paths:
            sum_ += int(path)
        return sum_
        