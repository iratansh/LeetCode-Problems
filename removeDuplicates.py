class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 2
        for i in range(2, len(nums)):
            nums[j] = nums[i]
            if nums[i] != nums[j - 2]:
                j += 1
        return min(len(nums), j)
