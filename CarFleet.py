class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        stack = []

        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))

        for p, s in sorted(pos_speed)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
