class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")
        sold = 0
        rest = 0

        for price in prices:
            prev_hold = hold
            prev_sold = sold

            hold = max(hold, rest - price)
            sold = prev_hold + price
            rest = max(rest, prev_sold)
        
        return max(sold,rest)

