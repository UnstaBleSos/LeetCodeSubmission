class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i,x in enumerate(nums):
            if x not in freq:
                freq[i]=x
            if freq[i] in freq:
                return True
        return False
        