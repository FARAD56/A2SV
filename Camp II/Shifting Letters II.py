class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ps = [0]*(len(s)+2)

        for a,b, k in shifts:
            val = -1 if not k else k
            ps[a+1] += val
            ps[b+2] -= val

        ps = list(accumulate(ps[1:len(s)+1]))

        ans = ''
        for idx, char in enumerate(s):
            ans += chr((ord(char)- ord('a') + ps[idx])%26 + ord('a'))

        return ans

        
