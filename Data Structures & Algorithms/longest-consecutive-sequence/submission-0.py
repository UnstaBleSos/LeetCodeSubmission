class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        max_sequence = 1
        sequence=1
        for x in range(1,len(sorted_nums)):
            if sorted_nums[x] == sorted_nums[x-1]:
                continue
            elif sorted_nums[x] == sorted_nums[x-1]+1:
                sequence+=1
                max_sequence=max(max_sequence,sequence)
            else:
                sequence=1
        
        return max_sequence
           
            