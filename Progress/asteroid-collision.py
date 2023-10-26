class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:

            while stack and stack[-1] > 0 > num:
                if stack[-1] < abs(num):
                    stack.pop()
                    continue
                elif stack[-1] == abs(num):
                    stack.pop()
                break
            else:
                stack.append(num)
        return stack