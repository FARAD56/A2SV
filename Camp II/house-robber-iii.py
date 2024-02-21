# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def attack(root):
            if not root:
                return 0 

            if not root.left and not root.right:
                return root.val

            if root not in memo:
                if root.left: a,b = attack(root.left.left), attack(root.left.right)
                else: a,b =0,0
                if root.right: c,d = attack(root.right.left), attack(root.right.right)
                else: c,d = 0,0
                memo[root] = max(root.val +a+b+c+d , attack(root.left) + attack(root.right))

            return memo[root]

        memo = {}
        return attack(root)