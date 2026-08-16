class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0 
        memo = {}
        freq = {}
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(alphabet)):
            freq[i+1] = alphabet[i]

        def dfs(position):
            if position == len(s):
                return 1

            if s[position] == "0":
                return 0

            if position in memo:
                return memo[position]

            ways = 0
            if "1" <= s[position] <= "9":
                ways += dfs(position+1) 
            
            if position+1< len(s):
                twodigits = s[position] + s[position+1]
                twodigits = int(twodigits)
                if 10 <= twodigits <= 26:
                    ways += dfs(position+2)
            memo[position] = ways
            return ways
            
        output = dfs(0)
        return output
