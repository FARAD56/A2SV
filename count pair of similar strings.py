class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter 
        from math import factorial
        new_set =[]
        for word in words:
            new_word = list(set(list(word)))
            new_set.append(new_word)

        string_list =[]
        for set1 in new_set:
            string = ''
            for i in range(len(set1)):
                string += set1[i]
            string_list.append(string)

        print(string_list)

        count = Counter(string_list)
        print(count)
        track = 0
        for key in count:
            if count[key] > 1:
                if count[key] == 2:
                    track += 1
                elif count[key] > 2:
                    permutation = factorial(count[key]) / (factorial(count[key]-2)*factorial(2))
                    track += int(permutation)

        return track