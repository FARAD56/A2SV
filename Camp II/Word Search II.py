class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTrie = Trie()
        front = defaultdict(set)
        Set = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                front[board[i][j]].add((i,j))

        maxi = float('-inf')
        for word in words:
            maxi = max(maxi, len(word))
            myTrie.insert(word)
            Set.update(front[word[0]])

        ans = set()

        def bfs(i,j):
            nonlocal ans
            path = {(i,j)}
            queue = [( i,j,board[i][j],path)]

            while queue:
                r,c, word, path = queue.pop()
                
                if myTrie.search(word):
                    ans.add(word)

                if len(word) < maxi and myTrie.prefix(word):
                    for rm,cm in [(1,0),(0,1),(-1,0),(0,-1)]:
                        if 0 <= r+rm < len(board) and 0 <= c+cm < len(board[0]) and (r+rm, c+cm) not in path:
                            queue.append((r+rm, c+cm, word+board[r+rm][c+cm], path|{(r+rm, c+cm)} ))

        for row, col in Set:
            bfs(row, col)
            if len(ans) == len(words): return words
        return list(ans)          
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children: return False
            else: curr = curr.children[char]
        return curr.is_end

    def prefix(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children: return False
            else: curr = curr.children[char]
        return True

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
