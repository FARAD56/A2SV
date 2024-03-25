class Solution:
    def longestPrefix(self, s: str) -> str:
        power = 1
        mod = 10**9 + 7
        sum_,sum_2 = 0,0
        ans = ''
        for i in range(len(s)-1):

            sum_ = (sum_*29 + ord(s[i]) - ord('a') + 1) % mod
            sum_2 = (sum_2 + (ord(s[-i-1]) - ord('a') + 1) * power ) % mod

            power = (power*29)%mod

            if sum_ == sum_2:
                ans = s[:i+1]

        return ans
        

        
