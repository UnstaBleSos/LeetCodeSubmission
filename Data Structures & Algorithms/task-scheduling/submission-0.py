class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks :
            return None

        freq= {}
        time = 0
        for i,x in enumerate(tasks):
            if x not in freq:
                freq[x] = 0
            freq[x] +=1
        maxHeap = []
        for i in freq:
            heapq.heappush(maxHeap,(-freq[i]))
        
        queue = deque()

        while maxHeap or queue:
            time += 1 
            if maxHeap:
                maxFrequency = heapq.heappop(maxHeap)
                frequency = -maxFrequency
                frequency -= 1
            else:
                frequency = None
            if frequency:
                queue.append((frequency, time+n))
            
            if queue and queue[0][1] == time:
                item = queue.popleft()
                heapq.heappush(maxHeap,-(item[0]))
        
        return time
            

        



            