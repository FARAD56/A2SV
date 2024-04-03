class ST:
    def __init__(self, nums, m):
        self.tree = [1] * (4 * len(nums))
        self.lazy = [1] * (4 * len(nums))
        self.arr = nums
        self.MOD = m
        self.build_tree(1, 0, len(nums) - 1)

    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(2 * node, start, mid)
            self.build_tree(2 * node + 1, mid + 1, end)
            self.tree[node] = (self.tree[2 * node] * self.tree[2 * node + 1]) % self.MOD

    def lazy_modify(self, node, start, end):
        if self.lazy[node] != 1:
            self.tree[node] = (self.tree[node] * self.lazy[node]) % self.MOD
            if start != end:
                self.lazy[2 * node] = (self.lazy[2 * node] * self.lazy[node]) % self.MOD
                self.lazy[2 * node + 1] = (self.lazy[2 * node + 1] * self.lazy[node]) % self.MOD
            self.lazy[node] = 1

    def query_range(self, node, start, end, l, r):
        self.lazy_modify(node, start, end)
        if start > end or start > r or end < l:
            return 1
        if start >= l and end <= r:
            return self.tree[node] % self.MOD
        mid = (start + end) // 2
        p1 = self.query_range(2 * node, start, mid, l, r)
        p2 = self.query_range(2 * node + 1, mid + 1, end, l, r)
        return (p1 * p2) % self.MOD

    def modify_range(self, node, start, end, l, r, val):
        self.lazy_modify(node, start, end)
        if start > end or start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[node] = (self.tree[node] * val) % self.MOD
            if start != end:
                self.lazy[2 * node] = (self.lazy[2 * node] * val) % self.MOD
                self.lazy[2 * node + 1] = (self.lazy[2 * node + 1] * val) % self.MOD
            return
        mid = (start + end) // 2
        self.modify_range(2 * node, start, mid, l, r, val)
        self.modify_range(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = (self.tree[2 * node] * self.tree[2 * node + 1]) % self.MOD

    def query(self, l, r):
        return self.query_range(1, 0, len(self.arr) - 1, l, r)

    def modify(self, l, r, val):
        self.modify_range(1, 0, len(self.arr) - 1, l, r, val)

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()

    new_seg = ST(a, m)

    l, r = 0, n - 1

    for i in range(n):
        print(new_seg.query(l, r), end=" ")
        if s[i] == 'L':
            l += 1
        elif s[i] == 'R':
            r -= 1

    print()

t = int(input())
for _ in range(t):
    solve()
