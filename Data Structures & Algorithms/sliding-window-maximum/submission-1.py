class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left =0
        freq={}
        for right in range(len(nums)):
           if len(nums[left:right+k]) == k: 
            freq[right] = max(nums[left:right+k])
            left+=1
           if right-left+1 < k:
            right+=1
        
        output = [1]*len(freq)
        for x in range(len(freq)):
            output[x] = freq[x]
        return output
                
                
                
           
        
        
        
        
        
        
            