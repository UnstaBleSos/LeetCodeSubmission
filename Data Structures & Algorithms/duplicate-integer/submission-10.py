class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(1,len(nums)):
            if nums[x] == nums[x-1]:
                return True
            return False