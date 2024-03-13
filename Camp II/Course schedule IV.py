class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[float('inf')]*numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            dist[i][i] = 0

        for src, dest in prerequisites:
            dist[src][dest] = 1

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        ans = []
        for x,y in queries:
            ans.append(dist[x][y] != float("inf"))

        return ans
