class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLength = len(s)
        tLength = len(t)

        if sLength != tLength:
            return False

        return sorted(s) == sorted(t)
       
        