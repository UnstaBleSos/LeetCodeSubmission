# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        q= deque([root])
        output = []

        while q:
            currentLevel = len(q)
            for i in range(currentLevel):
                node = q.popleft()

                if i == currentLevel-1:
                    output.append(node.val)    
                

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            
        return output