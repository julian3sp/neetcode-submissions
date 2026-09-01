class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        seen = []

        for i in range(len(prices)):
            profit = 0
            if seen:
                profit = prices[i] - min(seen)
            if profit > maxProfit:
                maxProfit = profit
            seen.append(prices[i])

        
        return maxProfit
        