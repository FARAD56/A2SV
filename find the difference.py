class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        char_freq = {}

        # Count the character frequencies in string s
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        # Compare the character frequencies in string t
        for char in t:
            if char in char_freq:
                char_freq[char] -= 1
            else:
                return char  # The character was added

        # Find the added character by checking the remaining frequency
        for char, freq in char_freq.items():
            if freq < 0:
                return char
