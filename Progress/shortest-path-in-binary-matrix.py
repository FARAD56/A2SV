class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([[(0,0),1]])

        if grid[0][0] == 1:
            return -1

        direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        visited = set()

        def check_movement(r,c,rm,cm):
            if (0 <= r+rm < len(grid)) and (0 <= c + cm < len(grid)) and grid[r+rm][c+cm]==0 and ((r+rm, c+cm)) not in visited:
                return True

        goal = (len(grid)-1,len(grid)-1)
        valid = []

        while queue:
            position, level = queue.popleft()
    
            if position == goal:
                valid.append(level)

            r,c = position
            for rm,cm in direction:
                if check_movement(r,c,rm,cm):
                    visited.add((r+rm,c+cm))
                    queue.append([(r+rm,c+cm),level+1])

        return min(valid) if valid else -1


