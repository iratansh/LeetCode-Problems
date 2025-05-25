class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # you can skip at most k 0s in each substring, variable sliding window problem
        skips = k
        maxLen = 0
              
        l = 0 # increment l <==> we have reached a num we can't skip
        for r in range(len(nums)):
            if nums[r] == 0 and skips == 0: # Case: no more skips, increment l until it passes a 0
                while nums[l] != 0: # will break when l = 0
                    l += 1
                l += 1 
                skips += 1
            if nums[r] == 0 and skips > 0:
                skips -= 1

            maxLen = max(maxLen, r - l + 1)
        return maxLenMax Consecutive Ones III
