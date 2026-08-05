class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        minDist = [float("inf")]*n
        minDist[0] = 0
        answer = 0 

        def manhattan(prev, current):
            px,py = prev
            x,y = current
            return (abs(px-x)+abs(py-y))

        for _ in range(n):
            best = float("inf")
            for i in range(n):
                if i in visited:
                    continue
                if minDist[i]<  best:
                    best = minDist[i]
                    current = i
            visited.add(current)
            answer+= best
            for j in range(n):
                if j in visited:
                    continue
                dist = manhattan(points[current],points[j])
                if dist<minDist[j]:
                    minDist[j] = dist
        
        return answer