class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeros, num_ones = 0, 0
        n_size = len(nums)
        for num in nums:
            if num == 0:
                num_zeros += 1
            elif num == 1:
                num_ones += 1
        
        for i in range(num_zeros):
            nums[i] = 0
        for i in range(num_zeros, (num_zeros + num_ones)):
            nums[i] = 1
        for i in range((num_zeros + num_ones), n_size):
            nums[i] = 2
