class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        incoming = defaultdict(int)
        g = defaultdict(list)
        for idx,lis in enumerate(graph):
            incoming[idx] = len(lis)
            for num in lis:
                g[num].append(idx)

        queue = deque()
        for key in incoming:
            if not incoming[key]:
                queue.append(key)

            
        ans = []
        while queue:
            leave = queue.popleft()
            ans.append(leave)
            for neighbour in g[leave]:
                incoming[neighbour] -= 1
                if not incoming[neighbour]:
                    queue.append(neighbour)
        ans.sort()
        return ans 
        