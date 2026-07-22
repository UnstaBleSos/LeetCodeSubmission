class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        path = {i:[] for i in range(n)}
        for node, edge in edges:
            path[node].append(edge)
            path[edge].append(node)
        
        visited = set()
        def dfs(edge,parent):
            visited.add(edge)
            for neighbour in path[edge]:
                if neighbour == parent:
                    continue
                elif neighbour in visited:
                    return False
                else:
                    if not dfs(neighbour,edge): 
                        return False 
            return True

        if not dfs(0,None):
            return False

        if len(visited) == n:
            return True
        else:
            return False