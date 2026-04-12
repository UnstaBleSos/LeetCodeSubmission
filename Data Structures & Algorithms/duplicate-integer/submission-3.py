class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y]:
                    return True
        return False