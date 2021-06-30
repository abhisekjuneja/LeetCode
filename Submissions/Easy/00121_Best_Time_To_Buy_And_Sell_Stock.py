# Difficulty: Easy
# Problem Statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buySellProfit = []
        minStockPrice = float('inf')
        for p in prices:
            minStockPrice = min(minStockPrice, p)
            buySellProfit += [p - minStockPrice]
        
        return max(buySellProfit)