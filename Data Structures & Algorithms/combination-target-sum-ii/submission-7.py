class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return None
        res = []
        path =[]
        nums = sorted(candidates)
        def combineSum(idx,remaining):
            if remaining == 0:
                res.append(path.copy())
                return 
            if remaining < 0:
                return 
            if idx == len(nums):
                return
            for i in range(idx,len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                combineSum(i+1,remaining- nums[i])

                path.pop()
        combineSum(0,target)
        return res
