class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[1]
        
        table = [0] * len(cost)
        table[0] = cost[0]
        table[1] = cost[1]
        for i in range(2, len(cost)):
            table[i] = cost[i] + min(table[i - 1], table[i - 2])
        
        return min(table[-1], table[-2])
