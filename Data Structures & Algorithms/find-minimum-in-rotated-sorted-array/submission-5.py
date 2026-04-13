class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 , len(nums)
        target = 1000
        while l<=r:
            mid = (l+r) // 2
            
            while nums[mid] >= nums[l]:
                l=mid+1
                target = min(target,nums[l])
            
            while num[mid] <= nums[r]:
                r=mid-1
                target=min(target,nums[r])

        print(target)
                
        
        

            
        
        
