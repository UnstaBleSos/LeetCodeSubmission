class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      minimum = prices[0]
      profit = 0
      for end in range(len(prices)):
        maxprofit = prices[end] - minimum
        if profit < maxprofit:
            profit = maxprofit
        if prices[end] < minimum:
            minimum = prices[end]
        
      return profit 