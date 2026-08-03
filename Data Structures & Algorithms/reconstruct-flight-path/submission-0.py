class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = defaultdict(list)
        for source, dest in tickets:
            path[source].append(dest)
        
        for src in path:        
            path[src].sort(reverse=True)
        
        output = []

        def dfs(node):
            while path[node]:
                dest = path[node].pop()
                dfs(dest)
            output.append(node)
        
        dfs("JFK")
        return output[::-1]