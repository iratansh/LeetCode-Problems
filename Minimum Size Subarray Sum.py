class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        min_len = float('inf')

        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while curr_sum >= target:  # find min window size
                curr_window_size = r - l + 1
                min_len = min(min_len, curr_window_size) 
                curr_sum -= nums[l] 
                l += 1
        return min_len if min_len != float('inf') else 0
