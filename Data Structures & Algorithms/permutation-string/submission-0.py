class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        left =0 
        freq = {}
        lengths1 = len(s1)
        for right in range(len(s1)):
            if s1[right] not in freq:
                freq[s1[right]] = 0
            freq[s1[right]] += 1
        
        freqs2 = {}
        for right in range(len(s2)):
            if s2[right] not in freqs2:
                freqs2[s2[right]] =0
            freqs2[s2[right]] +=1

            if right-left+1 > lengths1:
                freqs2[s2[left]] -= 1
                if freqs2[s2[left]] == 0:
                    freqs2.pop(s2[left])
                left+=1

            if freqs2 == freq:
                return True
            
        return False
        



            
               



