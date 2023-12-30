# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.left.val].append(node.val)
                graph[node.val].append(node.left.val)
                queue.append(node.left)
            if node.right:
                graph[node.right.val].append(node.val)
                graph[node.val].append(node.right.val)
                queue.append(node.right)

        new_queue = deque([(target.val,0)])
        ans = []
        visited = set([target.val])
        while new_queue:
            leave,level = new_queue.popleft()

            if level == k:
                ans.append(leave)
            elif level > k:
                break

            for neighbour in graph[leave]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    new_queue.append((neighbour, level+1))
        return ans
