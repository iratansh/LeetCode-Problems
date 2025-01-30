class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
          
        table = [0] * len(nums)
        table[0] = nums[0]
        for i in range(1, len(nums)):
            table[i] = max(nums[i], table[i - 1] + nums[i])
    
        return max(table)
