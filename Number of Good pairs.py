nums1 = [1,2,3,0,0,0]
m=6
n=3
nums2 = [2,5,6]

for i in range(n):
    nums1[n+i] = nums2[i]
nums1.sort()
print(nums1)