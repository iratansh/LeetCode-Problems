class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # if the amount of money cannot be made up by any combination of coins then return 0
        # dp[i] should represent the number of combinations that make up sum i?
        # base case: dp[0] = 1 since there is 1 way to make a sum of 0 coins?
        # recurrence: dp[i] += dp[i - c]
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]

        return dp[-1]
