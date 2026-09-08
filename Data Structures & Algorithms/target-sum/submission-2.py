class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total+target) %2 != 0:
            return 0
        positive = (total+target)//2

        dp = [0] * (positive+1)
        dp[0] = 1

        for num in nums:
            for i in range(positive, -1, -1):
                if i < num:
                    continue
                dp[i] = dp[i]+dp[i-num]
        
        return dp[positive]
