class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return []
        
        n = len(points)
        answer = 0
        minDist = [float("inf")]*n
        minDist[0] = 0
        visited = set()

        def manHatten(prev,current):
            px, py = prev
            x, y = current
            return abs(px-x)+abs(py-y)
        
        for _ in range(n):
            best = float("inf")
            for i in range(n):
                if i in visited:
                    continue
                
                if minDist[i] < best:
                    best = minDist[i]
                    current = i
            answer+=best
            visited.add(current)
            for j in range(n):
                if j in visited:
                    continue
                
                dist = manHatten(points[current], points[j])
                if dist < minDist[j]:
                    minDist[j]= dist
                
        
        return answer
