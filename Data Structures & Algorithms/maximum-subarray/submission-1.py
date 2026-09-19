class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        best_sum = nums[0]

        for i in range(1,len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            
            best_sum = max(current_sum, best_sum)
        
        return best_sum