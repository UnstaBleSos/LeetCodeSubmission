# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None or k < 0:
            return None
        
        self.counter = 0
        def calMinimum(root,k):
            if root == None or k<0:
                return None
            
           

            left = calMinimum(root.left,k)

            self.counter +=1
            if self.counter == k:
                return root.val

            right = calMinimum(root.right,k)

            return left or right
        
        result = calMinimum(root,k) 

        return result

        
        