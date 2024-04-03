from collections import defaultdict
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char)- ord("A")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def insert2(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children2:
                curr.children2[char] = TrieNode()
            curr = curr.children2[char]
        curr.is_end = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char in curr.children2: curr = curr.children2[char]
            else: return False
        return curr.is_end
    
    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char in curr.children2: curr = curr.children2[char]
            else: return False
        return True

# todo

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.children2 = defaultdict(TrieNode)
