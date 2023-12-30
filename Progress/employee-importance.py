"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        Dict = defaultdict(list)

        for employee in employees:
            Dict[employee.id] = [employee.importance,employee.subordinates]
            
        ans = 0
        def dfs(vertex):
            nonlocal ans
            ans += Dict[vertex][0]
            if not Dict[vertex][1]:
                return 0

            for neighbour in Dict[vertex][1]:
                dfs(neighbour)

        dfs(id)
        return ans
