class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sortNums = sorted(nums)
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = (right + left) // 2

            if sortNums[mid] == target:
                return mid
            elif sortNums[mid] < target:
                left = mid + 1
            else:
                right  = mid - 1 
        
        return -1
           

        