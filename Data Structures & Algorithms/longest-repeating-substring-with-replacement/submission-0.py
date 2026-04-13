class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0 
        window_length = 0
        max_frequency = 0
        max_length = 0 
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 0
            freq[s[right]] +=1
            max_frequency = max(max_frequency,freq[s[right]])
            if right-left+1 - max_frequency <= k:
                max_length = max(max_length, right-left+1)
            else:
                freq.pop(s[right])
                left+=1
        return max_length

            

    
        
        
           
            
           
                