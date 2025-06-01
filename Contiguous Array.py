class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq = defaultdict(int) 
        freq[0] = -1
        running_sum = 0
        maxLen = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        for i, num in enumerate(nums):
            running_sum += num
            if running_sum in freq:
                start = freq[running_sum]
                length = i - start
                maxLen = max(maxLen, length)
            else:
                freq[running_sum] = i
        return maxLen
