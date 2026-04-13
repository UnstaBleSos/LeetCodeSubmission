class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i,x in enumerate(nums):
            if x not in freq:
                freq[i]= x
                return True
        return False
        