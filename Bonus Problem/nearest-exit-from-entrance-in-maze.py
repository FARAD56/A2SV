class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        visited = set([tuple(entrance)])
        queue = deque([(tuple(entrance),0)])

        def inbound(row, col):
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and (row,col) not in visited and maze[row][col] == '.':
                return True

        short = float("inf")
        while queue:
            pos , level = queue.popleft()
            r , c = pos

            if [r,c] != entrance and (r == 0 or r== len(maze)-1 or c == 0 or c == len(maze[0])-1):
                short = min(short, level)

            for rm, cm in directions:
                if inbound(r+rm, c+cm):
                    visited.add((r+rm, c+cm))
                    queue.append(((r+rm,c+cm),level +1))
        return short if short != float("inf") else -1
