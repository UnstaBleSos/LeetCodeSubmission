class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        if n == 0:
            return False
        minimum = 1000
        for i in range(n):
            nums = [nums[-1]] + nums[:-1]
            minimum = min(nums,minimum)
        
        return minimum
            
        
        
