class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = nums[0]
        left, right = 0, len(nums)-1
        while left<=right:
            if nums[left]<nums[right]:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid]> target:
                    left = mid+1
                else:
                    right = mid-1
            
            if nums[left]>= nums[right]:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid]>target:
                    left = mid+1
                else:
                    right = mid -1


        return -1