class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
        path = []
        def checkPalindrome(word) -> bool:
            l,r = 0, len(word)-1
            while l<r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def backTrack(idx):
            if idx == len(s): #forgot to add base condition
                res.append(path.copy())
                return
            for i in range(idx,len(s)):
                candidate= s[idx:i+1]#mistake subcandidate
                if checkPalindrome(candidate):
                    path.append(candidate)
                    backTrack(i+1)
                    path.pop()
        backTrack(0)
        return res