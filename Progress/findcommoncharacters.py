class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        if not words:
            return ans

        # Count the occurrences of each character in the first word
        char_count = {}
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1

        # Iterate through the characters of the first word
        for char in char_count:
            min_count = char_count[char]
            # Check if the character is present in all words
            for i in range(1, len(words)):
                count = words[i].count(char)
                min_count = min(min_count, count)
            # Append the character to the result list the minimum number of times it appears
            ans.extend([char] * min_count)

        return ans