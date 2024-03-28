class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prevSmaller = [-1]*len(heights)
        nextSmaller = [len(heights)]*len(heights)

        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()     
            if stack: prevSmaller[i] = stack[-1]
            stack.append(i)
            
        stack = []
        for i in range(len(heights)):                 
            while stack and heights[stack[-1]] >= heights[i]:
                stackTop = stack.pop()
                nextSmaller[stackTop] = i
            stack.append(i)

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i] * (nextSmaller[i] - prevSmaller[i] -1)) 
        return max_area

                