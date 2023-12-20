class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        incoming = defaultdict(int)
        graph = defaultdict(set)
        for crs, pre in prerequisites:
            incoming[crs] += 1
            incoming[pre] += 0
            graph[pre].add(crs)

        for i in range(numCourses):
            incoming[i] += 0

        ans = []
        queue = deque()
        for key in incoming:
            if not incoming[key]:
                queue.append(key)

        print(graph)
        print(incoming)

        visited = set() 
        while queue:
            leave = queue.popleft()
            ans.append(leave) 
            for neighbour in graph[leave]:
                incoming[neighbour] -= 1
                if incoming[neighbour]==0:
                    queue.append(neighbour)

        
        return ans if len(ans) == numCourses else []


        

        