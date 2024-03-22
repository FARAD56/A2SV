class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        need,m,n = 0,len(needle),len(haystack)
        for i in range(m):
            need = need*29 + (ord(needle[i]) - ord('a')+1) % 1000000007
        
        hay = 0
        for i in range(n):
            hay = hay*29 + (ord(haystack[i]) - ord('a')+1) % 1000000007

            if i >= m:
                hay -= (ord(haystack[i-m]) - ord('a')+1)*(29**m)

            if hay == need:
                return i-m+1
                
        return -1
