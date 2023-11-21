# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        heapify(ans)

        def solve(root):
            nonlocal ans
            if not root:
                return

            solve(root.left)
            heappush(ans, -root.val)
            if len(ans) > k:
                heappop(ans)
            solve(root.right)
        solve(root)

        print(ans)
        return -ans[0]


