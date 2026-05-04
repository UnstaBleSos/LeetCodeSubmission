class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        arr=[]

        while l<=r:
            if (nums[l]*nums[l])> (nums[r]*nums[r]):
                arr.append((nums[l]*nums[l]))
                l+=1
            else:
                arr.append((nums[r]*nums[r]))
                r-=1
             
        
        return arr[::-1]