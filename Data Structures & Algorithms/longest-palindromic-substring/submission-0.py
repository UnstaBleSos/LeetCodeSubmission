class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest = ""
        for center in range(len(s)):
            l,r = center, center

            while l>= 0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1 
            oddString = s[l+1:r]
            if len(longest)<len(oddString):
                longest = oddString
            l,r = center, center+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1 
            evenString = s[l+1:r]
            if len(longest)<len(evenString):
                longest = evenString
        
        return longest


            

        

        