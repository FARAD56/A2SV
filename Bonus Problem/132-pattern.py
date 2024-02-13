class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minVal = float('inf')

        for num in nums:

            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and stack[-1][1] < num:
                return True

            minVal = min(minVal, num)
            stack.append([num, minVal])
                
        return False