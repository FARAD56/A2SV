class Solution:
    def br(self,nums,target):
        y = len(nums)
        l, r = 0, len(nums)-1
        while l <= r :
            middle = (l + r)//2
            if nums[middle] > target:
                y= middle
                r = middle -1
            else:
                l = middle + 1
        return y

    def bl(self,nums, target):
        x = len(nums)
        l, r = 0, len(nums)-1
        while l <= r :
            middle = (l + r)//2
            if nums[middle] >= target:
                x= middle
                r = middle -1
            else:
                l = middle + 1
        return x

    def check(self, nums, target):
        l,r = 0,len(nums)-1
        while l <= r:
            middle = (l+r)//2
            if nums[middle] > target:
                r = middle -1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return True

        return False
        
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        x,y = self.bl(nums,target), self.br(nums,target)-1
        return [x,y] if self.check(nums,target) == True else [-1,-1]
        


   
