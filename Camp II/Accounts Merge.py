class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        myUnion = UnionFind(accounts)

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])-1):
                myUnion.union(accounts[i][j], accounts[i][j+1])

        soln,ans = defaultdict(list), []
        for key in myUnion.parents:
            soln[myUnion.find(key)].append(key)

        for sol in soln:
            ans.append([myUnion.name[sol]] + sorted(soln[sol]))
        
        return ans

class UnionFind:
    def __init__(self, accounts):
        self.parents = {}
        self.name = {}
        for i in range(len(accounts)):
            for account in accounts[i][1:]:
                self.parents[account] = account
                self.name[account] = accounts[i][0]
    
    def find(self, account):
        if account == self.parents[account]:
            return account
        self.parents[account] = self.find(self.parents[account])
        return self.parents[account]

    def union(self, a, b):
        repA, repB = self.find(a), self.find(b)

        if repA < repB:
            self.parents[repB] = repA
        else:
            self.parents[repA] = repB

        
