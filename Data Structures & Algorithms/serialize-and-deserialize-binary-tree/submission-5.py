# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        
        q= deque([root])
        out = []
        while q:
            node = q.popleft()
            if node:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                out.append('N')

        
        return ",".join(out)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
           return None
        
        q = data.split(",")
        root = TreeNode(int(q[0]))
        
        queue = deque([root])
        i = 1
        while queue :
            node = queue.popleft()

            if q[i]!= "N":
                node.left = TreeNode(int(q[i]))
                queue.append(node.left)
            i+=1

            if q[i]!= "N":
                node.right = TreeNode(int(q[i]))
                queue.append(node.right)
            i+=1
        
        return root
        
        
        
        
            













        
