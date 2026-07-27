class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return []
        
        path = {i:[] for i in range(n)}
        for node1, node2 in edges:
            path[node1].append(node2)
            path[node2].append(node1)
        visited = set()
        output = 0

        def dfs(edge):
            if edge in visited:
                return
            
            visited.add(edge)
            for neighbor in path[edge]:
                if neighbor not in visited:
                    dfs(neighbor)

        for edge in range(0,n):
            if edge not in visited:
                output+=1
                dfs(edge)
        
        return output