class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        Dict,ans = {0:-1},len(nums)
        ps = [0] + list(accumulate(nums))

        if not ps[-1]%p: return 0

        for idx,num in enumerate(ps):
            Dict[num%p] = idx
            curr = (num-ps[-1])%p

            if curr in Dict:
                ans = min(ans, idx-Dict[curr])
        
        return ans if ans != len(nums) else -1

