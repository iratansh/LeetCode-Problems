class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * n
        dp[0] = min(costs[0], costs[1], costs[2])

        for i in range(1, n):
            ptr7, ptr30 = i, i
            while ptr7 > 0 and days[ptr7 - 1] >= days[i] - 6:
                ptr7 -= 1

            while ptr30 > 0 and days[ptr30 - 1] >= days[i] - 29:
                ptr30 -= 1

            dp[i] = min(
                dp[i - 1] + costs[0],
                (dp[ptr7 - 1] if ptr7 > 0 else 0) + costs[1],
                (dp[ptr30 - 1] if ptr30 > 0 else 0) + costs[2]
            )

        return dp[n - 1]
