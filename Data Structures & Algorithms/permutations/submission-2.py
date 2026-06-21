class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        path = []
        used = [False]*len(nums)
        def findPermutes():
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            
            for i in range(len(nums)):
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True
                    findPermutes()
                    path.pop()
                    used[i]= False
        
        findPermutes()
        return res