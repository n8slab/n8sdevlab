class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell, hold = 0, -float("inf")

        for price in prices:
            sell = max(sell, hold + price)
            hold = max(hold, sell - price)

        return sell