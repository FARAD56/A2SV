class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-ele for ele in stones]
        heapify(stones)
        
        while len(stones) > 1:
            a = heappop(stones)
            b = heappop(stones)
            heappush(stones, -abs(a-b))
        
        return abs(stones[0])

