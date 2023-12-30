class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])
        while queue:

            node = queue.popleft()
            visited.add(node)

            for val in rooms[node]:
                if val not in visited:
                    queue.append(val)
        
        vis_check = set([0])

        for room in rooms:
            for val in room:
                vis_check.add(val)
        return len(visited) == len(vis_check)