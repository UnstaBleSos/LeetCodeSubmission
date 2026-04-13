class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return False
        minimum = 1000
        for i in range(len(nums)):
            nums = nums[-i:] + nums[:-i]
            minimum = min(nums[i],minimum)
        
        return minimum
