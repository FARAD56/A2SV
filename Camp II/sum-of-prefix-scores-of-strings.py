class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        myTrie = Trie()
        ans = []
        for word in words:
            myTrie.insert(word)
        
        for word in words:
            ans.append(myTrie.search(word))
        return ans

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1
    
    def search(self, prefix):
        curr = self.root
        count = 0
        for char in prefix:
            curr = curr.children[char]
            count += curr.count
        return count

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(TrieNode)
        self.count = 0