class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        res = []
        path = []
        word = ""

        def checkPalindrome(subStr) -> bool:
            l,r = 0 ,len(subStr)-1
            while l<r:
                if subStr[l] != subStr[r]:
                    return False
                l+=1
                r-=1
            
            return True
        
        def backTrack(idx):
            if idx == len(s):
                res.append(path.copy())
                return
            
            for i in range(idx,len(s)):
                word = s[idx:i+1]
                if checkPalindrome(word):
                    path.append(word)
                    backTrack(i+1)
                    path.pop()
        
        backTrack(0)
        return res

       
            