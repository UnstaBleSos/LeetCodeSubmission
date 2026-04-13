class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left =0
        freq={}
        for right in range(len(nums)):
            if len(nums[right:k+right]) == k:
                freq[right] = max(nums[right:k+right])

        output = [1]*len(freq)
        for x in range(len(freq)):
            output[x] = freq[x]
        
        return output
        
        
        
        
        
            