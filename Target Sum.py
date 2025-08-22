class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # this is a tricker problem, looks like 1D DP + Backtracking? I'm wondering if it's either OR, or both?
        # at each iteration we are given the choice to pick between +-
        # this looks similar to the previous 1D DP questions i've done, we should iterate from target backwards
        # dp[i] should store the number of ways to make the sum of i?

        # count the number of subsets that sum to P where P = (target + total_sum) // 2
        total_sum = sum(nums)
        if total_sum < abs(target) or (target + total_sum) % 2 == 1:
            return 0

        P = (target + total_sum) // 2
        dp = [0] * (P + 1)
        dp[0] = 1 # since there is 1 way to get a sum of 0: take nothing

        for num in nums:
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[P] 
