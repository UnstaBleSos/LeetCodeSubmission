class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        n = len(edges)
        path = {i:[] for i in range(n)}
        def dfs(node1,node2):

            if node1 == node2:
                return True

            if node1 not in path:
                return False
            
            visited.add(node1)
            for neighbor in path[node1]:
                if neighbor not in visited:
                    if dfs(neighbor,node2):
                        return True
            
            return False

        for node1, node2 in edges:
            visited = set()
            if dfs(node1,node2):
                return [node1,node2]
            else:
                if node1 not in path:
                    path[node1] = []
                if node2 not in path:
                    path[node2] = []
            
                path[node1].append(node2)
                path[node2].append(node1)