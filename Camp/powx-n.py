class Solution:
    def myPow(self, x: float, n: int) -> float:

        def PowP(x,n):
            if n < 1:
                return 1
            return PowP(x*x,n//2) if 0 == n%2 else x*PowP(x*x,(n-1)//2)
       
        return PowP(x,abs(n)) if n > 0 else 1/(PowP(x,abs(n)))
        


