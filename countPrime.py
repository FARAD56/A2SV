class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 0 <= n <= 5 *(10**6): 
            prime_count = 0
            for j in range(2,n):
                flag = 0
                for i in range(2, int(sqrt(j)+1)):
                    if j % i == 0:
                        flag = 1
                        break
                if flag == 0:
                    prime_count += 1

            return prime_count
            
                