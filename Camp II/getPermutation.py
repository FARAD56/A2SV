class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # def backtrack(word):
        #     if len(word) == n:
        #         soln.append(int(''.join(word)))
        #         return

        #     for i in range(1,n+1):
        #         i = str(i)
        #         if i not in word:
        #             word.append(i)
        #             backtrack(word)
        #             word.remove(i)

        # soln = []
        # backtrack([])
        soln = list(permutations(range(1,n+1)))
        return ''.join(str(i) for i in soln[k-1])

