class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        min = prices[0]
        profit = -prices[0]
        prices.pop(0)

        for val in prices:
            if val - min > profit:
                profit = val - min
            if val < min:
                min = val
        if profit > 0:
            return profit
        return 0
