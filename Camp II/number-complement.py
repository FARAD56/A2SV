class Solution:
    def findComplement(self, num: int) -> int:
        ans = ''

        num = bin(num)[2:]

        for char in num:
            ans += "1" if char == "0" else "0"

        return int(ans,2)