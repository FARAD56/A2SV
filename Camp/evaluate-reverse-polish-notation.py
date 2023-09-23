class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for item in tokens:
            if item not in '+*/-':
                s.append(int(item))
            else:
                a = int(s.pop())
                b = int(s.pop())
                if item == '+': s.append(b+a)
                elif item == '*': s.append(b*a)
                elif item == '-': s.append(b-a)
                else: s.append(b/a)
        return int(s[0])