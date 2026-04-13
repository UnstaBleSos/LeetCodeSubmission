class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       slen = s.len()
       tlen = t.len()
       if slen != tlen:
            return False
       if sorted(s) == sorted(t):
            return True
