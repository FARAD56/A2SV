class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(curr, idx, word):
            if idx == len(word): return curr.is_end
            if word[idx] != '.':
                if word[idx] in curr.children and dfs(curr.children[word[idx]], idx+1, word): return True
            else:
                for char in curr.children:
                    if dfs(curr.children[char], idx + 1, word): return True
            return False
            
        return dfs(self.root, 0, word)

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(TrieNode)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)