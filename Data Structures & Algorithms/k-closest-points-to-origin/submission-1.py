class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if points == None:
            return 0

        distances = []
        minDistances=[]
        for i in points:
            distance = i[0]**2 + i[1]**2
            if len(distances) < k:
                heapq.heappush(distances,(-distance,[i[0],i[1]]))
            else:
                currentDistance= (distances[0][0])
                if  -distance > currentDistance:
                    heapq.heappop(distances)
                    heapq.heappush(distances,(-distance,[i[0],i[1]]))
        
        while len(distances) > 0:
            toppoint = heapq.heappop(distances)
            minDistances.append(toppoint[1])
        return minDistances