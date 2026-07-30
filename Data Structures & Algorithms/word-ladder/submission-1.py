class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque()
        words = set(wordList)

        if endWord not in wordList:
            return 0
        
        if beginWord in words:
            words.remove(beginWord)
        
        q.append((beginWord,1))
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while q:
            currentWord, length = q.popleft()
            if currentWord == endWord:
                return length
                    
            for i in range(len(currentWord)):
                for ch in alphabet:
                    newWord = currentWord[:i] + ch + currentWord[i+1:]
                    if newWord in words:
                        words.remove(newWord)
                        q.append((newWord,length+1))
            
        return 0

