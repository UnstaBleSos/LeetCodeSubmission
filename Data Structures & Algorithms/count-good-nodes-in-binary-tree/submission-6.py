# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        self.maximumValue = root.val
        self.goodNodesCount = 0

        def countNodes(root,maxSoFar):
            if root == None:
                return 0
            
            if root.val >= maxSoFar:
                maxSoFar = max(maxSoFar,root.val)
                self.goodNodesCount +=1
            
            left = countNodes(root.left,maxSoFar)
            right = countNodes(root.right,maxSoFar)

        countNodes(root,self.maximumValue)

        return self.goodNodesCount
