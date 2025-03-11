class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return 0
        
        jumps = 0
        l, r = 0, 0  

        while r < len(nums) - 1: 
            farthest_index = 0
            for i in range(l, r + 1):  
                farthest_index = max(farthest_index, i + nums[i])

            l = r + 1 
            r = farthest_index
            jumps += 1  

        return jumps
