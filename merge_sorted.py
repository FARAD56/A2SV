def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1 += nums2
        nums1 = nums1

        nums1 = [item for item in nums1 if item != 0]
        nums1.sort()

        return nums1

print(merge([0],0,[1],1))