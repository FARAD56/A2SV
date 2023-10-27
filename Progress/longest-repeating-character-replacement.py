class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Dict = defaultdict(int)
        leng = 0
        start = 0
        for i in range(len(s)):
            Dict[s[i]] += 1
            window = i - start + 1
            max_count = max(Dict.values())
            if (window-max_count) > k:
                Dict[s[start]] -= 1
                start += 1
            leng = max(leng, i-start+1)
        return leng



            

