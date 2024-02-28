class Solution:
    def longestCommonPrefix(self, strs):
        myTrie = Trie()
        myTrie.insert(strs[0])
        longest = float("inf")

        for word in strs:
            longest = min(longest,myTrie.search(word))

        print(longest)
        return strs[0][:longest]



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
        for idx,char in enumerate(word):
            if char in curr.children: curr = curr.children[char]
            else: return idx
        return len(word)



class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(TrieNode)
