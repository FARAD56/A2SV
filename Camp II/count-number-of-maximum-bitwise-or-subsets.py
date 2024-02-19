class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def bitwise_or(state):
            val = 0
            for num in state:
                val |= num
            return val

        total = bitwise_or(nums)    

        def f(index, t):
            ans.append(list(t))
            
            for i in range(index, len(nums)):
                t.append(nums[i])
                f(i + 1, t)
                t.pop()

        ans = []
        nums.sort()
        f(0, [])
        count = 0
        for sub in ans:
            count += (bitwise_or(sub) == total)
        
        return count

