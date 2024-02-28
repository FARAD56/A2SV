class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children2:
                curr.children2[char] = TrieNode()
            curr = curr.children2[char]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char in curr.children2: curr = curr.children2[char]
            else: return False
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr.children2: curr = curr.children2[char]
            else: return False
        return True


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children2 = defaultdict(TrieNode)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
