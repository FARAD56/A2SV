# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l_range,r_range = [float("-inf"),root.val], [root.val,float("inf")]

        def comp(l_range, r_range, root):
            if not root:
                return True

            if root.right:
                if not (r_range[0] < root.right.val < r_range[1]):
                    return False
                res1 = comp([r_range[0],root.right.val],[root.right.val,r_range[1]],root.right)
            else:
                res1 = True
                
            if root.left:
                if not (l_range[0] < root.left.val < l_range[1]):
                    return False
                res2 =comp([l_range[0],root.left.val],[root.left.val,l_range[1]],root.left)
            else:
                res2 = True
            return res1 and res2
        return comp(l_range,r_range,root)
            