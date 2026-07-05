class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        return self.findNode(curr,0,word)
        
    
    def findNode(self,node, idx, word):
        if idx == len(word):
            return node.isWord
        
        ch = word[idx]
        if ch == ".":
            for child in node.children:
                if self.findNode(node.children[child],idx+1,word):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            node = node.children[ch]
            return self.findNode(node,idx+1,word)
    
            







        
