class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        Dict = defaultdict(list)
        for s,d in edges:
            Dict[s].append(d)
            Dict[d].append(s)

        min_n = 0
        visited = set()
        def dfs(vertex, visited):
            if vertex in visited:
                return

            if vertex and len(Dict[vertex]) == len(Dict)-1:
                return vertex

            visited.add(vertex)
            for neighbour in Dict[vertex]:
                ans = dfs(neighbour, visited)
                if ans:
                    return ans

        return dfs(edges[0][0],visited)
                
