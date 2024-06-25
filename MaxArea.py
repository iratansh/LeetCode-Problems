class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_pointer, r_pointer = 0, len(height) - 1

        area = 0
        while l_pointer < r_pointer:
            res = (r_pointer - l_pointer) * min(height[l_pointer], height[r_pointer])
            area = max(area, res)
            if height[l_pointer] < height[r_pointer]:
                l_pointer += 1
            else:
                r_pointer -= 1
        return area
