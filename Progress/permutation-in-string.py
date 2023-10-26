class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1) , len(s2)
        s1_count = Counter(s1)
        s2_sub_count = Counter(s2[:m])

        if s2_sub_count == s1_count:
            return True

        for l in range(n-m):
            r = l + m 

            s2_sub_count[s2[r]] += 1
            s2_sub_count[s2[l]] -= 1

            if s2_sub_count == s1_count:
                return True

        return False
