class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        Dict = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    Dict[i+1].append(j+1)
        
        visited = set()
        def dfs(vertex, visited):
            if vertex in visited:
                return False

            visited.add(vertex)
            for neighbour in Dict[vertex]:
                if neighbour not in visited:
                    a = dfs(neighbour,visited)
                    if a:
                        return a

        count = 0
        for key in Dict:
            if dfs(key, visited) == None:
                count += 1
                
        return count
