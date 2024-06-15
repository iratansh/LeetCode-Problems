class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        profit = 0
        for el in prices[1::]:
            if el > price:
                profit = max(profit, el - price)
            else:
                price = el
        return profit
