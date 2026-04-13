class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i,x in enumerate(nums):
            if x not in freq:
                freq[x]= x
            if x in freq:
                return True
        return False
        