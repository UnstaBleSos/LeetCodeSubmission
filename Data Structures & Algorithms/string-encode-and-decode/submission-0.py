class Solution:

    def encode(self, strs: List[str]) -> str:
        count =0
        encoded =""
        for x in strs:
            count=len(x)
            encoded += f"{count}#"+x
        return encoded

    
    def decode(self, s: str) -> List[str]:
        i =0
        decoded=[]
        while i<len(s):
            stringLength = ""
            while s[i]!="#":
                stringLength += s[i]
                i+=1
            lengthInt = int(stringLength)
            i+=1
            word = s[i: lengthInt+i]
            decoded.append(word)
            i+=lengthInt
        print(decoded)
        return decoded






