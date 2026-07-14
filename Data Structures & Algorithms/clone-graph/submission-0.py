"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {} 
        def dfs(node):
            if node is None:
                return None
            
            if node in copies:
                return copies[node]

            clone = Node(node.val)

            copies[node] = clone

            for neighbors in node.neighbors:
                cloneNeighbor = dfs(neighbors)
                clone.neighbors.append(cloneNeighbor)
            
            return copies[node]

        return dfs(node)




        