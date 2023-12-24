from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = (max_profit, profit)
            else:
                buy = sell
            sell += 1

        return max_profit


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))