class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i,x in enumerate(nums):
            if x not in freq:
                freq[i]=x
            if x in freq:
                return True
        return False
        