# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([(root,0)])
        levels = [[]]

        while queue:
            node, level = queue.popleft()

            if level < len(levels):
                levels[level].append(node.val)
            else:
                levels.append([node.val])

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        avs = []
        for level in levels:
            avs.append(sum(level)/len(level))
        
        return avs
            
        