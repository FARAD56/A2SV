class Solution:
    def climbStairs(self, n: int) -> int:
         
        cs = {}
        
        def comp(n):
            if n in cs:
                return cs[n]

            if n < 4:
                return n
            else:
                result = comp(n-1) + comp(n-2)
                cs[n] = result
            return result
        return comp(n)
                
            
        