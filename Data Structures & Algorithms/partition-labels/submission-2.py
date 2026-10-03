class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []

        freq= {}
        start = 0 
        end = 0 
        result = []
        
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 0
            freq[s[i]] = i
        
        for i in range(len(s)):
            if freq[s[i]] > end:
                end = freq[s[i]]

            if i == end:
                result.append(end-start+1)
                start = end + 1 

        return result


