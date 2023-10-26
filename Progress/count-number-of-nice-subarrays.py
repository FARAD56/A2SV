class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        Dict = defaultdict(int)
        Dict[0] = 1
        curr,count = 0,0
        for num in nums:
            if num % 2 == 1:
                curr += 1
            count += Dict[curr-k]
            Dict[curr] += 1
        return count
            

