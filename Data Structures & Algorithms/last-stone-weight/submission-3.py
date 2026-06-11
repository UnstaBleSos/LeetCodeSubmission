class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0 
        weights =[]
        for stone in stones:
            heapq.heappush(weights,-stone)
        while len(weights) > 1:
            x = heapq.heappop(weights)
            y = heapq.heappop(weights)
            
            if x==y:
                continue
            elif x < y:
                lastweight = heapq.heappush(weights, -(y-x))
            else:
                lastweight = heapq.heappush(weights,-(x-y))
            
        return -(heapq.heappop(weights)) if weights else 0


        