class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        path = {i:[] for i in range(1,n+1)}
        for source, target, time in times:
            path[source].append((target,time))
        
        dist = {i:float("inf") for i in range(1,n+1)}
        dist[k] = 0
        min_heap = [(0,k)]
        while min_heap:
            distance, target = heapq.heappop(min_heap)
            if distance > dist[target]:
                continue
            for neighbor, weight in path[target]:
                if distance+weight < dist[neighbor]:
                    dist[neighbor] = distance+weight
                    heapq.heappush(min_heap,((distance+weight), neighbor))
            
        if float("inf") in dist.values():
            return -1
        else: return max(dist.values())
        