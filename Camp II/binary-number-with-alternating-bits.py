class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = ''

        while n:
            a += str(n&1)
            n >>= 1

        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                return False
        return True