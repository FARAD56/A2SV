class Solution:
    def maxProduct(self, words: List[str]) -> int:
        len_char = []
        for word in words:
            len_char.append((len(word), set(word)))
        ans = 0

        for i in range(len(words)):
            for j in range(len(words)):
                check = True
                for char in len_char[i][1]:
                    if char in len_char[j][1]: 
                        check = False
                        break
                if check: ans = max(ans, len_char[i][0]*len_char[j][0])
        return ans
