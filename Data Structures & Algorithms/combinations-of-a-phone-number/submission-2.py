class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        path =[]
        choice = ""
        freq = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
        def combineDigits(idx):
            if len(digits) == len(path):
                res.append("".join(path.copy()))
                return

            currentDigit = digits[idx]
            for i in freq[currentDigit]:
                path.append(i)
                combineDigits(idx+1)
                path.pop()


            return res
        combineDigits(0)
        return res
        
        
       