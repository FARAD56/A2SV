class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
            
        fb = [0]*(n+1)
        fb[2] = fb[1] = 1

        for i in range(3,n+1):
            fb[i] = fb[i-1] + fb[i-2] + fb[i-3]

        return fb[-1]
        