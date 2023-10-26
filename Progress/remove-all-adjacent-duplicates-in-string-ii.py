class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        Dict = defaultdict(int)
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1]==k: 
                    stack.pop()
            else:
                stack.append([char,1])
        return ''.join(var[0]*var[1] for var in stack)