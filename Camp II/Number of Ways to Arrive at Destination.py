class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for src, dest, cost in roads:
            graph[src].append((dest, cost))
            graph[dest].append((src, cost))

        heap = [(0, 0)]
        heapify(heap)
        visited = set()

        memo = {}
        cost = {}

        while heap:
            cos, node = heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            cost[node] = cos

            for child in graph[node]:
                if child[0] not in visited:
                    heappush(heap, (child[1] + cos, child[0]))

        target = cost[n-1]
        print(cost)
        
        def dfs(path_sum, node):
            if not node: return 1

            if node in memo:
                return memo[node]

            res = 0
            for child, cos in graph[node]:
                if path_sum + cost[child] + cos == target:
                    res += dfs(path_sum + cos, child)%(10**9+7)

            memo[node] = res
            return memo[node]
        
        return dfs(0,n-1)%(10**9+7)
