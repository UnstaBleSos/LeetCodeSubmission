class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i,x in enumerate(nums):
            if x in freq:
                return True
            else: 
                freq[i]=x
        return False
        