class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        farthest = 0
        count = 0 
        current_end = 0
        for i in range(len(nums)):
            jump = i + nums[i]
            farthest = max(jump, farthest)

            if i == current_end:
                count += 1
                current_end = farthest 

            if current_end >= len(nums) -1:
                break

        return count  
        
        
