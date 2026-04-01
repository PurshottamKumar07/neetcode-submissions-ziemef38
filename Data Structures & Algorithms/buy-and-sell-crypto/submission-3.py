class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = set()
        buy = 0
        for sell in range(len(prices)):
            if prices[sell] < prices[buy] and prices[buy] > prices[sell]: 
                buy = sell
            else: 
                profit.add(prices[sell] - prices[buy])
        if not profit: 
            return 0
        else: 
            return max(profit)