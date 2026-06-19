class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return None
        path=[]
        res =[]
        def dfs(index,remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            
            if remaining <0:
                return
            
            if index == len(nums):
                return

            path.append(nums[index])
            dfs(index,remaining-nums[index])

            path.pop()
            dfs(index+1,remaining)

        dfs(0,target)
        return res

            