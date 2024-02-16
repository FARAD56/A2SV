class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x,y = bin(x)[2:], bin(y)[2:]
        maxi = max(len(x),len(y))
        x, y = '0'*(maxi - len(x))+x, '0'*(maxi - len(y))+y

        count = 0

        for i in range(maxi):
            count += (x[i]!=y[i])

        return count