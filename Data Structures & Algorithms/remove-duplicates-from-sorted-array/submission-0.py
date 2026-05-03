class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        l,r =0,1
        while r<n:
            if nums[l] == nums[r]:
                r+=1
                continue
            nums[l+1] = nums[r]
            count+=1
            l+=1
        
        return count
           