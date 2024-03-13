class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dest = [[float("inf")]*n for _ in range(n)]

        for i in range(n):
            dest[i][i] = 0

        for src, dist, cost in times:
            dest[src-1][dist-1] = cost


        ans = float("-inf")
        for m in range(n):
            for i in range(n):
                for j in range(n):
                    dest[i][j] = min(dest[i][j], dest[i][m] + dest[m][j])

        return max(dest[k-1]) if max(dest[k-1]) != float("inf") else -1

        

