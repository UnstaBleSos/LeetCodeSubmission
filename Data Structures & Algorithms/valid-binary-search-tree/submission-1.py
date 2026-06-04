# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        self.low,self.high = float('-inf'), float('inf')
        self.currentRoot = root.val
        def checkChildren(root,low,high):
            if root == None:
                return True
            
            if not(low<root.val<high):
                return False
                
            left = checkChildren(root.left,low,root.val)
            right = checkChildren(root.right,root.val,high)

            return left and right
        
        if checkChildren(root,self.low,self.high):
            return True
        else:
            return False