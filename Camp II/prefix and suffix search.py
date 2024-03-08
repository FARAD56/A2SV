class WordFilter:

    def __init__(self, words: List[str]):
        self.myTrie = Trie(words)

        for idx, word in enumerate(words):
            for i in range(len(word)):
                self.myTrie.insert(word[i:]+'#'+word, idx)

    def f(self, pref: str, suff: str) -> int:
        return self.myTrie.search(suff+'#'+pref)
        

class Trie:
    def __init__(self,words):
        self.words = words
        self.root = TrieNode()

    def insert(self, word, index):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                curr.children[char].index = index
            curr = curr.children[char]
            curr.index = index

        curr.index = index

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children: return -1
            else: curr = curr.children[char]
        return curr.index

class TrieNode:
    def __init__(self):
        self.index = -1
        self.children = {}


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
