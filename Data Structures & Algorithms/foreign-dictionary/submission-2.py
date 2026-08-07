class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ordering =[]
        n = len(words)
        path = {}
        visited = {}

        for word in words:
            for ch in word:
                path[ch] = set()

        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]
            j=0
            
            while j<len(word1) and j <len(word2):
                if word1[j]!=word2[j] :
                    path[word1[j]].add(word2[j])
                    break
                j+=1

                if j == len(word2) and len(word1)> len(word2):
                    return ""
        
        
        def dfs(word):
            visited[word] = "visiting"

            for adjacent in path[word]:
                if adjacent not in visited:
                    if not dfs(adjacent):
                        return ""
                elif visited[adjacent] == "visiting":
                    return ""
                elif visited[adjacent] == "visited":
                    continue
            visited[word] = "visited"
            ordering.append(word)
            return True

        for letter in path:
            if letter not in visited:
               if not dfs(letter):
                    return ""
        
        string =  list(reversed(ordering))
        return "".join(string)
            