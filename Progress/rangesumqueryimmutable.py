class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.pre_sum = []
        self.nums = nums
        self.total = 0
        for num in self.nums:
            self.total += num
            self.pre_sum.append(self.total)
        print(self.pre_sum)

    def sumRange(self,left,right):
        if left == 0:
            return self.pre_sum[right]
        return self.pre_sum[right] - self.pre_sum[left-1] 