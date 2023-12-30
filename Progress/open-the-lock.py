class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([('0000',0)])
        deadends = set(deadends)
        visited = set(['0000'])

        if '0000' in deadends:
            return -1

        while queue:
            value,level = queue.popleft()

            if value == target:
                return level

            for i in range(4):
                ref = list(value)
                ref[i] = str((int(ref[i])+1)%10)
                ref = ''.join(ref)
                if ref not in deadends and ref not in visited:
                    visited.add(ref)
                    queue.append((ref,level+1))

                ref = list(value)
                if ref[i] > '0':
                    ref[i] = str((int(ref[i])-1))
                else:
                    ref[i] = '9'
                ref = ''.join(ref)
                if ref not in deadends and ref not in visited:
                    visited.add(ref)
                    queue.append((ref,level+1))

        return -1