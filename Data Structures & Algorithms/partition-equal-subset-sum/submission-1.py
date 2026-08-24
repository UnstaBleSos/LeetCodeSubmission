class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
       
        total = sum(nums)
        
        if total %2 != 0 :
            return False

        target = total//2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                if dp[i-num] == True:
                    dp[i] = True 
        
        if dp[target]:
            return True
        else:
            return False