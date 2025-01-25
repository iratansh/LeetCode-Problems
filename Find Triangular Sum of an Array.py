class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1: # continue until len nums == 1
            newNums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
            nums = newNums 
        return nums[0]  
