class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        path = []
        def findPermutes():
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    findPermutes()
                    path.pop()
        
        findPermutes()
        return res