class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        Dict = defaultdict(list)
        for s,d in edges:
            Dict[s].append(d)
            Dict[d].append(s)

        visited = set()
        def dfs(vertex, visited):
            if vertex == destination:
                return True

            visited.add(vertex)

            for neighbour in Dict[vertex]:
                if neighbour not in visited:
                    valid = dfs(neighbour, visited)
                    if valid:
                        return valid

        return dfs(source,visited)
            