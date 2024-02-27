class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = defaultdict(int)

        for num in arr:
            dic[num] = dic[num-difference] + 1

        return max(dic.values())

        
            