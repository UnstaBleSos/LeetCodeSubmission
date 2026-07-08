class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        path = set()
        output = set()
        row, col = len(board) , len(board[0])

        for ch in words:
            curr = root
            for chars in ch:
                if chars not in curr.children:
                    curr.children[chars] = TrieNode()
                curr = curr.children[chars]
            curr.isWord = True
        pointer = root
        def backTrack(r,c,pointer,word):
            if pointer.isWord == True:
                output.add(word)
                
            if r >= row or c >= col:
                return False
            
            if r<0 or c<0:
                return False
            
            if (r,c)in path:
                return False

            if board[r][c] not in pointer.children:
                return False
            else:
                pointer = pointer.children[board[r][c]]

            path.add((r,c))
            word+= board[r][c]
            backTrack(r+1,c,pointer,word)
            backTrack(r-1,c,pointer,word)
            backTrack(r,c+1,pointer,word)
            backTrack(r,c-1,pointer,word)
            path.remove((r,c))
        
        for i in range(row):
            for j in range(col):
                backTrack(i,j,root,"")
        
        return list(output)
        