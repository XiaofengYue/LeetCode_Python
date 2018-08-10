class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        profit = 0
        for val in prices:
            if val < buy:
                buy = val
            elif val > buy:
                profit += val - buy
                buy = val
        return profit
