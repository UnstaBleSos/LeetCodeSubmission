class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        def robHouse(houses):
            n = len(houses)
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2,n):
                dp[i] = max(
                    dp[i-1],
                    dp[i-2] + houses[i]
                )

            return dp[n-1]

        left = robHouse(nums[:-1])
        right = robHouse(nums[1:])

        return max(left,right)
