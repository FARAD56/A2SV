class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0,len(letters)-1
        gt = letters[0]
        while l <= r:
            middle = (l+r)//2
            if letters[middle] > target:
                r = middle -1
                gt = letters[middle]
            else:
                l = middle + 1
        return gt