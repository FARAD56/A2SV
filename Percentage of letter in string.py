class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        s = s.lower()
        letter = letter.lower()
        percentage = float(s.count(letter)* 100/len(s)) 
        percentage = int(percentage)
        return percentage