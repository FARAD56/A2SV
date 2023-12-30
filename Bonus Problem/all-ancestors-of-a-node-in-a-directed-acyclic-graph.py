class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        incoming = defaultdict(int)
        link = defaultdict(list)
        graph = defaultdict(set)
        for src,dest in edges:
            incoming[dest]+= 1
            incoming[src] += 0
            graph[dest].add(src)
            link[src].append(dest)

        queue = deque()

        for key in incoming:
            if not incoming[key]:
                queue.append(key)

        ans = [[] for i in range(n)]
        while queue:
            leave = queue.popleft()

            array = set()

            for neighbour in link[leave]:
                incoming[neighbour] -= 1
                if not incoming[neighbour]:
                    queue.append(neighbour)

            for parent in graph[leave]:
                array.add(parent)
                array.update(ans[parent])

            ans[leave] = sorted(list(array))
        
        return ans


