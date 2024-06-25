class Solution:
    def trap(self, height: List[int]) -> int:
        l_pointer, r_pointer = 0, len(height) - 1
        h_l, h_r = height[l_pointer], height[r_pointer]
        vol = 0

        while l_pointer < r_pointer:
            if h_l < h_r:
                l_pointer += 1
                h_l = max(height[l_pointer], h_l)
                vol += h_l - height[l_pointer]
            else:
                r_pointer -= 1
                h_r = max(height[r_pointer], h_r)
                vol += h_r - height[r_pointer]
        return vol
