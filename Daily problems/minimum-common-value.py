class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if nums2[0] > nums1[-1] or nums1[0] > nums2[-1]:
            return -1
        for num in nums1:
            if num in nums2:
                return num
        return -1