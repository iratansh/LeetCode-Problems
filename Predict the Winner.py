class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        
        for length in range(2, n + 1):  # subarray lengths
            for i in range(n - length + 1):
                j = i + length - 1
                pickLeft = nums[i] - dp[i + 1][j]
                pickRight = nums[j] - dp[i][j - 1]
                dp[i][j] = max(pickLeft, pickRight)
        
        # If the score difference is >= 0, player 1 can win
        return dp[0][n - 1] >= 0
