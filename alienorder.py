class Solution(object):
    def isAlienSorted(self,words, order):
        alphabet = {}
        for i, char in enumerate(order):
            alphabet[char] = i

        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            j = 0
            while j < len(word1) and j < len(word2):
                if word1[j] != word2[j]:
                    if alphabet[word1[j]] > alphabet[word2[j]]:
                        return False
                    break
                j += 1

            if j == len(word2) and j < len(word1):
                return False

        return True