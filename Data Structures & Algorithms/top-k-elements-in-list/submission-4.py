class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        
        output = []
        maxHeap = []
        freq ={}

        for i,x in enumerate(nums):
            if x not in freq:
                freq[x] = 0
            freq[x] += 1
        
        for i in freq:
            heapq.heappush(maxHeap,(-freq[i],i))
        
        while maxHeap and len(output) < k:
            top = heapq.heappop(maxHeap)
            output.append(top[1])
        
        return output
        
