class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for i in range(len(graph)):
            g[i] = graph[i]
        
        output = []
        def dfs(root,path):
            nonlocal output
            if root == len(graph)-1:
                output.append(path)

            for neighbour in g[root]:
                dfs(neighbour, path+[neighbour])
        dfs(0,[0])
        return output