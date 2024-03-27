class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        nextGreater = [-1]*len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                stackTop = stack.pop()
                nextGreater[stackTop] = i-stackTop

            stack.append(i)

        for i in range(len(nextGreater)):
            nextGreater[i] = 0 if nextGreater[i] == -1 else nextGreater[i]

        return nextGreater