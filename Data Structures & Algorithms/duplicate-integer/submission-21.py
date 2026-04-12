class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      sortednums= sorted(nums)
      for x in range(1,len(sortednums)):
        if sortednums[x] == sortednums[x-1]:
            return True

      return False