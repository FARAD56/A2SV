class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for key in count:
            heap.append([-count[key],key])
        heapify(heap)

        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])

        return ans

        