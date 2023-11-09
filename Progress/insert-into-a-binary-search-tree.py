# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self , root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root

        def comp(par,val,current):
            if not current:
                if par.val < val:
                    par.right = TreeNode(val)
                else:
                    par.left = TreeNode(val)
                return


            if val < current.val:
                comp(current,val,current.left)
            else:
                comp(current,val,current.right)

        if not root:
            return TreeNode(val)
        comp(root,val,current)
        return root