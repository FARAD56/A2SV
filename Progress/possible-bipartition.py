class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        Dict = defaultdict(list)

        for src, dest in dislikes:
            Dict[src].append(dest)
            Dict[dest].append(src)

        color = [0]+([-1]*(n))
        def dfs(node):
            for neighbour in Dict[node]:
                if color[neighbour] == -1:
                    if color[node] == 0:
                        color[neighbour] = 1
                    else:
                        color[neighbour] = 0
                    if not dfs(neighbour):
                        return False
                else:
                    if color[node] ==  color[neighbour]:
                        return False
            return True

        for node in Dict:
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
        return True




            
            
            
                    