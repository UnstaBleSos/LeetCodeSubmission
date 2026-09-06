class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(amount+1):
                remaining = i - coin

                if remaining < 0 :
                    continue

                if i < 0 :
                    continue
                
                dp[i] = dp[i] + dp[remaining]
        return dp[amount]