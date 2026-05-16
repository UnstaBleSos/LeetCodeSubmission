class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      ssort = sorted(s)
      tsort = sorted(t)

      if ssort == tsort:
        return True
      else:
        return False
        