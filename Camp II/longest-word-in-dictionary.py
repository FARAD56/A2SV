class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        myTrie = Trie()

        longest = 0
        wor = ''
        for word in words:
            if len(word) == 1:
                myTrie.insert(word)
                if not longest: longest, wor = 1, word
            elif len(word) > 1 and myTrie.search(word[:-1]):
                myTrie.insert(word)
                if len(word) > longest: longest, wor = len(word), word

        return wor



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

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(TrieNode)