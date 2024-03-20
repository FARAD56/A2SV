class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        Set = set()
        for num in range(2,int(n**(0.5))+1):
            if num not in Set:
                for i in range(num**2, n, num):
                    Set.add(i)

        return sum([1 for num in range(2,n) if num not in Set])
