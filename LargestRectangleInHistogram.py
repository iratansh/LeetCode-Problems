class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                area = max(area, (i - index) * height)
                start = index
            stack.append((h, start))    

        for h, i in stack:
            area = max(area, h * (len(heights) - i))
        return area
