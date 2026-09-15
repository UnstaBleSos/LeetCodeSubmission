class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)] 

        for i in range(2, n):
            for j in range(0,n-i):
                r = j + i
                for k in range(j+1,r):
                    dp[j][r] = max(dp[j][r], dp[j][k] + nums[j]*nums[k]*nums[r] 
                    + dp[k][r] )
        
        return dp[0][n-1]