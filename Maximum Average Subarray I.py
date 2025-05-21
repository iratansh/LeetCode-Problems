class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # basically find the subarray with the largest sum because all subarrays will be divided by the same value (k)
        maxSum = currSum = sum(nums[:k])
        for r in range(k, len(nums)):
            currSum += nums[r] - nums[r - k] # update currSum and compare
            maxSum = max(maxSum, currSum)
        return maxSum / k 
