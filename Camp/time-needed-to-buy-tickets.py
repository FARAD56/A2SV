class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        if tickets[k] == 1:
            return k + 1
        else:
            for idx,num in enumerate(tickets):
                if num >= tickets[k]:
                    if idx > k:
                        total += (tickets[k]-1)
                    else:
                        total += tickets[k]
                else:
                    total += num
            return total