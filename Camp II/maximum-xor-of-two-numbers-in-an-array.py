class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        myTrie = Trie()
        max_bit = max(nums).bit_length()
        for num in nums:
            val = 0 if num else -1
            conver = '0'*(max_bit- num.bit_length()+val) + bin(num)[2:]
            myTrie.insert(conver)
        
        maxi = 0
        for i in range(len(nums)):
            val = 0 if nums[i] else -1
            conver = '0'*(max_bit- nums[i].bit_length()+val) + bin(nums[i])[2:]
            best = myTrie.search(conver)
            maxi = max(maxi, nums[i]^best)
            if maxi == (2**max_bit)-1: return maxi
        return maxi

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
        val = ''
        for char in word:
            opp = str(1-int(char))
            if opp not in curr.children:
                val += char; curr = curr.children[char]
            else:
                val += opp; curr = curr.children[opp]
        return int(val, 2)

            

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}