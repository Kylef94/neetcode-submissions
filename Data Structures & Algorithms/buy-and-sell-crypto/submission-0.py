class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            sell = prices[i]
            buy = min(prices[:i])
            profit = max(profit, sell - buy)
        return profit
        