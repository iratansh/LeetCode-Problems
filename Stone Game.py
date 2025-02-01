class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = piles[i]
        
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                dp[start][end] = max(
                    piles[start] - dp[start + 1][end],
                    piles[end] - dp[start][end - 1]
                )
                
        return dp[0][n - 1] > 0
