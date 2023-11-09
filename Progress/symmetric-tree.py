# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def comp(r_node, l_node):
            if not r_node and not l_node:
                return True

            if not r_node or not l_node or r_node.val != l_node.val:
                return False

            return comp(r_node.right, l_node.left) and comp(r_node.left, l_node.right)

        return comp(root.right, root.left)