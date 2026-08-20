class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
       
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                newWord = s[i:j]
                if newWord in wordDict and dp[j] is True: 
                    dp[i] = True
        
        return dp[0]
            