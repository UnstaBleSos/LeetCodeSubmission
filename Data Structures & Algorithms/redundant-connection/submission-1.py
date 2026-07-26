class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        
        graph = {}
        def dfs(node1, node2):

            if node1 == node2:
                return True

            if node1 not in graph:
                return False
            visited.add(node1)

            for neighbor in graph[node1]:
                if neighbor not in visited:
                    if dfs(neighbor,node2):
                        return True
            
            return False

        for node1, node2 in edges:
            visited = set()
            if dfs(node1,node2):
                return [node1,node2]
            else:
                if node1 not in graph:
                    graph[node1] =[]
                if node2 not in graph:
                    graph[node2] =[]

                graph[node1].append(node2)
                graph[node2].append(node1)

