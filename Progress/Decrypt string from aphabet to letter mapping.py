class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        import string 

        integer_range = range(1,10)
        integer_range2 = range(10,27)
        char_range = string.ascii_lowercase[:9]
        char_range2 = string.ascii_lowercase[9:]

        mapped = dict(zip(char_range,integer_range))
        mapped2 = dict(zip(char_range2,integer_range2))

        for key in mapped2:
            mapped2[key] = str(mapped2[key])
            mapped2[key] += '#'

        mapped.update(mapped2)
        mapped

        inpt = s
        res = inpt
        for key in reversed(list(mapped)):
            com = str(mapped[key])
            if com in inpt:
                res = res.replace(com,key)
            
        return res