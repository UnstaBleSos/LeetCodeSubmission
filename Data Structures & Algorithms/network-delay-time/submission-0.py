class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        path = {i:[] for i in range(1,n+1)}

        for source, target, time in times:
            path[source].append((target,time))

        dist = {i:float("inf") for i in range(1,n+1)}
        dist[k] = 0
        min_heap = [(0,k)]
        while min_heap:
            distance, node = heapq.heappop(min_heap)

            if distance > dist[node]:
                continue
            
            for neighbor, weight in path[node]:
                new_distance = distance + weight
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))


        if float("inf") in dist.values():
            return -1

        return max(dist.values())
                