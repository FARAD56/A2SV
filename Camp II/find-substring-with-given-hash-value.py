class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s,sub,ans,p = s[::-1],0,'',pow(power, k-1, modulo)
        
        for i in range(len(s)):
            sub = sub if i < k else (sub - ((ord(s[i-k])-96)*p))%modulo 
            sub *= power
            sub = (sub + ord(s[i])-96)%modulo

            if sub % modulo == hashValue:
                ans = s[i-k+1:i+1][::-1]

        return ans
            

            


            


