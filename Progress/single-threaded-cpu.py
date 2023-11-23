class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task = [[task,idx] for idx,task in enumerate(tasks)]
        heapify(task)
        ans = []
        processing = []
        heapify(processing)

        i = task[0][0][0]

        while task:

            while task and i >= task[0][0][0]:
                curr = heappop(task)
                heappush(processing, [curr[0][1],curr[1]])

            if processing:
                time, idx = heappop(processing)
                i += time
                ans.append(idx)
            else:
                i = max(i,task[0][0][0])

        for _ in range(len(processing)):
            time, idx = heappop(processing)
            ans.append(idx)

        return ans

        


