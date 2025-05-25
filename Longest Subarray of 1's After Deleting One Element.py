class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = maxLen = 0
        num_zeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > 1:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            maxLen = max(maxLen, r - l)             
        return maxLen
