from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, nums, k):
        win = defaultdict(int)
        win[0] = 1
        count = curr = 0

        for num in nums:
            curr += num
            count += win[curr%k]
            win[curr%k] += 1

        return count
