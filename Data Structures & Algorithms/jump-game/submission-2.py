class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        farthest = 0 
        for i in range(len(nums)):
            if i > farthest:
                return False
            
            jump = i + nums[i]
            farthest = max(jump, farthest)

            if farthest >= len(nums) -1:
                return True
        