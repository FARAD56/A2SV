class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None (modifies nums1 in-place)
        """
        last_merged = m + n - 1
        last_nums1 = m - 1
        last_nums2 = n - 1
        
        while last_nums2 >= 0:
            if last_nums1 >= 0 and nums1[last_nums1] > nums2[last_nums2]:
                nums1[last_merged] = nums1[last_nums1]
                last_nums1 -= 1
            else:
                nums1[last_merged] = nums2[last_nums2]
                last_nums2 -= 1
            last_merged -= 1