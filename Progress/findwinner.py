class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import Counter
        winners = {}
        losers = {}

        for win,lose in matches:
            winners[win] = winners.get(win, 0) + 1
            losers[lose] = losers.get(lose, 0) + 1

        print(losers)

        win_list = [win for win in winners if win not in losers]
        lose_list = [lose for lose in losers if losers[lose] == 1]

        win_list.sort()
        lose_list.sort()
                
        return [win_list,lose_list]


