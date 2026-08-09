class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        path = {i:[] for i in range(n)}

        for fromcity,tocity,price in flights:
            path[fromcity].append((tocity,price))
        row,col = n,k+2
        dist = [[float("inf")]*col for _ in range(row)]
        dist[src][0] = 0
        min_heap = [(0,src,0)]

        while min_heap:
            price,node, flight = heapq.heappop(min_heap)

            if price > dist[node][flight]:
                continue
            
            if flight == k+1:
                continue

            for neighbor,amt in path[node]:
                if price+amt < dist[neighbor][flight+1]:
                    dist[neighbor][flight+1] = price+amt
                    heapq.heappush(min_heap,(price+amt, neighbor,flight+1))
        
        finalcost = dist[dst]
        if all(value == float("inf") for value in finalcost):
            return -1
        else:
            return min(finalcost)
            


