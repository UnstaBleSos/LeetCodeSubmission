class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None
        res = []
        path =[]
        nums = sorted(nums)
        def dfs(start):
            
            res.append(path.copy())
            
            for i in range(start,len(nums)):
                if i> start and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return res