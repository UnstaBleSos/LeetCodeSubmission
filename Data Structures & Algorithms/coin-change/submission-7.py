class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        if amount == 0:
            return 0

        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        
        for i in range(1,amount+1):
            for coin in coins:
                remaining = i - coin
                if remaining >= 0:
                    candidate = dp[remaining] + 1
                    if candidate < dp[i]:
                        dp[i] = candidate

        
        return -1 if dp[amount] == float("inf") else dp[amount]