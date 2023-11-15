# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if root == p or root == q:
            return root

        root1 = self.lowestCommonAncestor(root.left,p,q)
        root2 = self.lowestCommonAncestor(root.right,p,q)

        if root1 and root2:
            return root
        elif root1 and not root2:
            return root1
        else:
            return root2
        