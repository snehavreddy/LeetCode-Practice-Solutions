class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minProfit = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < minProfit:
                minProfit = prices[i]
            else:
                profit = prices[i] - minProfit
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
        