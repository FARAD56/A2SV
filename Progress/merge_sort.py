def merge(nums1, nums2):
    res = []
    i,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1

    if i < len(nums1):
        res += nums1[i:]
    if j < len(nums2):
        res += nums2[j:]

    return res

def merge_sort(nums):
    n = len(nums)

    if n <= 1:
        return nums
        
    nums1,nums2 = nums[:n//2],nums[n//2:]
    return merge(merge_sort(nums1),merge_sort(nums2))

print(merge_sort([1,5,3,4,2,6,9,7,8,0]))

