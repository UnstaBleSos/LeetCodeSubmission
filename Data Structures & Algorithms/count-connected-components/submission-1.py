class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        path = {i:[] for i in range(n)}
        for node,edge in edges:
            path[node].append(edge)
            path[edge].append(node)
        
        component = 0
        visited = set()

        def dfs(edge):
            visited.add(edge)

            for neighbor in path[edge]:
                if neighbor not in visited:
                    dfs(neighbor)


        for edge in range(0,n):
            if edge not in visited:
                component+=1
                dfs(edge)
        
        return component