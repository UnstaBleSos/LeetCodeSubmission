class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            letter = 'abcdefghijklmnopqrstuvwxyz'
            z=tuple([word.count(c) for c in letter])
            if z not in groups:
                groups[z]=[]
            groups[z].append(word)
        return list(groups.values())
            

           