class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float("inf")] * (amount + 1)
        table[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    table[i] = min(table[i], 1 + table[i - c])
        
        return table[amount] if table[amount] != float("inf") else -1
