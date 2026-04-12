class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left =0 
        formed = 0
        freq1={}
        freq2 = {}
        minString = ""
        minlength = float('inf')
        for right in range(len(t)):
            if t[right] not in freq1:
                freq1[t[right]] = 0
            freq1[t[right]] +=1
        
        required = len(freq1)
        for right in range(len(s)):
            if s[right] not in freq2:
                freq2[s[right]] =0
            freq2[s[right]] +=1 

            if s[right] in freq1 and freq1[s[right]] == freq2[s[right]] :
                formed+=1

            while formed == required: 
                if right-left+1 < minlength:
                    minlength = right-left+1
                    minString = s[left:right+1] 
                freq2[s[left]] -= 1
                if s[left] in freq1 and  freq2[s[left]] < freq1[s[left]]: 
                    formed-=1
                left+=1
                
           
        return minString

                
                