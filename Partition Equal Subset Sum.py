class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # this looks like a 1D DP question where dp[i] = bool represents whether it is possible to reach sum i using some of the numbers so far?
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)

        dp[0] = True # since sum 0 is always possible by choosing nothing
        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]
