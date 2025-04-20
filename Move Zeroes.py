class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        while l < len(nums) and nums[l] != 0:
            l += 1
        r = l + 1

        while l < len(nums) and r < len(nums) and l <= r:
            if nums[l] != 0:
                l += 1
            elif nums[l] == 0 and nums[r] != 0:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l += 1
            r += 1
